from tkinter import *
import os
from pygame import mixer
import  tkinter.messagebox
from tkinter import filedialog


root=Tk()
def about_us():
    tkinter.messagebox.showinfo("music player","plays music")
def browse_file():
    global filename
    filename=filedialog.askopenfilename()
    print(filename)


menubar=Menu(root)
root.config(menu=menubar)
subMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="file",menu=subMenu)

subMenu.add_command(label="open",command=browse_file)

subMenu.add_command(label="exit",command=root.destroy)
subMenu=Menu(menubar,tearoff=0)
menubar.add_cascade(label="help",menu=subMenu)
subMenu.add_command(label="aboutus",command=about_us)

mixer.init()
root.geometry('600x600')
root.title("melody")
text=Label(root,text="lets make some noise")
text.pack()


def play_but():
    try:
        pause#if pause is false goes to except else goes to else block
    except NameError:
        try:
            mixer.music.load(filename)
            mixer.music.play()
            statusbar['text']="playing music"+" "+os.path.basename(filename)
        except:
            tkinter.messagebox.showinfo("error","file not found")
            print("error")
    else:

        mixer.music.unpause()
        statusbar['text']="music resumed"
def stop_but():
    mixer.music.stop()
    statusbar['text']="music stopped"
def set_vol(val):
    volume=int(val)/100
    mixer.music.set_volume(volume)
def pause_but():
    global pause
    pause=TRUE

    mixer.music.pause()
    statusbar['text']="music paused"
muted=FALSE
def mute_but():
    global muted
    if muted:
        mixer.music.set_volume(0.7)
        speakerbtn.configure(image=speakerphoto)
        scale.set(70)
        statusbar['text']="music playing"
    else:
        mixer.music.set_volume(0)
        speakerbtn.configure(image=mutephoto)
        scale.set(0)
        statusbar['text'] = "music muted"
        muted=TRUE



middleframe=Frame(root)
middleframe.pack(padx=10,pady=10)
playphoto=PhotoImage(file='jazz.png')
playbtn=Button(middleframe,text='play',command=play_but,image=playphoto)
playbtn.pack(side=LEFT,padx=10)


stopphoto=PhotoImage(file='stop.png')
stopbtn=Button(middleframe,text='stop',command=stop_but,image=stopphoto)
stopbtn.pack(side=LEFT,padx=10)

pausephoto=PhotoImage(file='pause.png')
pausebtn=Button(middleframe,text='pause',command=pause_but,image=pausephoto)
pausebtn.pack(side=LEFT,padx=10)
scale=Scale(root,from_=0,to=100,orient='horizontal',command=set_vol)

rewindphoto=PhotoImage(file='rewind.png')
rewindbtn=Button(root,text='rewind',command=play_but,image=rewindphoto)
rewindbtn.pack()
mutephoto=PhotoImage(file='mute.png')
speakerphoto=PhotoImage(file='speaker.png')
speakerbtn=Button(root,text='speaker',command=mute_but,image=speakerphoto)
speakerbtn.pack()
scale=Scale(root,from_=0,to=100,orient='horizontal',command=set_vol)
scale.set(70)
mixer.music.set_volume(0.7)

statusbar=Label(root,text="welcome to melody",relief=SUNKEN)
statusbar.pack(side=BOTTOM,fill=X)
scale.pack()

root.mainloop()
