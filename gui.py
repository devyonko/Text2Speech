from gtts import gTTS
import os
from tkinter import *

def text2speech():
    text=entry.get()
    language='hi'
    output=gTTS(text=text,lang=language,slow=False)
    output.save("speechedVoice09.mp3")
    os.system('start speechedVoice09.mp3')

root=Tk()
canvas=Canvas(root,width=400,height=300)
canvas.pack()

entry=Entry(root)
canvas.create_window(200,180,window=entry)

btn=Button(text="Read aloud",command=text2speech)
canvas.create_window(200,230,window=btn)

root.mainloop()