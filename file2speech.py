from gtts import gTTS
import os


tetext=open('demo.txt','r').read()
language="en"
op=gTTS(text=tetext,lang=language, slow=True)

op.save("fileop.mp3")
os.system('start fileop.mp3')