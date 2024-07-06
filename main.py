from gtts import gTTS
import os


text="Lol this is very funyy"

output=gTTS(text=text,lang='en',slow=False)

output.save("test.mp3")

os.system("start test.")