
import pyttsx3 as tts

engine = tts.init()

text = input("\ntype the text: ")

#speed setting:
speed = input("choose the speed of audio (slow ,normal ,fast): ").lower()
speed_rate = {
    "slow" : 80 ,
    "normal" : 200 ,
    "fast" : 300 
}

engine.setProperty("rate" ,speed_rate[speed])

#voice setting:
voice_gender = int(input("choose the gender (0=male ,2=female): "))

voices = engine.getProperty('voices')
engine.setProperty("voice" ,voices[voice_gender].id)

#voice run:
engine.say(text)
engine.runAndWait()