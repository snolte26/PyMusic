import os
import time
import tkinter as tk
from tkinter import *
from tkinter import ttk
from pygame import mixer
from mutagen.mp3 import MP3

root = tk.Tk()
root.geometry('400x300')
root.resizable(False, False)
root.title('Music Player')

musicButtonY = 10
mixer.init()

def musicTime(song):
    audio = MP3(song)
    songLength = round(audio.info.length)
    remaining = songLength
    for i in range(songLength):
        timeLeft = "Time Remaining: " + str(remaining) + " seconds"
        songTime.delete('1.0', END)
        songTime.insert(INSERT, timeLeft)
        songTime.update()
        time.sleep(1)
        remaining -= 1
    pass

def playMusic(name):
    directory = os.path.dirname(os.path.abspath(__file__)) + "\\Music\\" + name
    print("Playing: " + name)
    '''
    chosen = name
    # audio = MP3(chosen)
    chosenSong = directory + "\\" + chosen
    playsound(chosenSong)
    '''

    mixer.music.stop()
    mixer.music.load(directory)
    mixer.music.play()

    musicTime(directory)




text = tk.Text(root, wrap="none")
vsb = tk.Scrollbar(orient="vertical", command=text.yview)
text.configure(yscrollcommand=vsb.set)
vsb.pack(side="right", fill="y")
text.pack(fill="both", expand=True)


play_button = ttk.Button(
    root,
    text='Resume',
    command=lambda: mixer.music.unpause()
)

play_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
play_button.place(
    x=300,
    y=10
)

pause_button = ttk.Button(
    root,
    text='Pause',
    command=lambda: mixer.music.pause()
)

pause_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
pause_button.place(
    x=300,
    y=40
)
stop_button = ttk.Button(
    root,
    text='Stop',
    command=lambda: mixer.music.stop()
)

stop_button.pack(
    ipadx=5,
    ipady=5,
    expand=True
)
stop_button.place(
    x=300,
    y=70
)

songTime = tk.Text(root, width=15, height=2)
songTime.place(
    x=250,
    y=125
)

directory = os.path.dirname(os.path.abspath(__file__)) + "\\Music"
songs = os.listdir(directory)
songList = []
for i in songs:
    if '.mp3' in i:
        i = i.replace('.mp3', '')
        songList.append(i)
    else:
        continue
for i in songList:
    b = tk.Button(
        root,
        text=str(i),
        command=lambda i=i: playMusic(str(i + '.mp3'))

    )
    text.window_create("end", window=b)
    text.insert("end", "\n")
    musicButtonY += 30

text.configure(state="disabled")
root.mainloop()
