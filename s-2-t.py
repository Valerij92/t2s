from gtts import*
import os

myText = "When you were here before. Couldn't look you in the eye"

language = 'en'

output =gTTS (text=myText, lang=language, slow=False)

output.save("out.mp3")

os.system("start output.mp3")