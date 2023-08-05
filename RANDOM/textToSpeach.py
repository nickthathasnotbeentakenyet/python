import gtts
from playsound import playsound # playsound==1.2.2

text = "Я пришел из будущего!"
mp3_file = "speach.mp3"
tts = gtts.gTTS(text=text,lang="ru")
tts.save(mp3_file)
playsound(mp3_file)
