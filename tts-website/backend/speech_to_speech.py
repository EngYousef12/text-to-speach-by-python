import pyttsx3 as tts
from text_to_speech import speak
from speech_to_text import speech_to_text as stt

command = input("tts = text to speech\nsts = speech to speech\nend = exit\nchoose a command: ")


if command == "tts":
    text = input("Enter the text you want to convert to speech: ")
    gender = int(input("Enter the gender of the voice (0 = male/ 2 =female): "))
    speed = input("Enter the speed of the voice (slow ,normal ,fast): ")
    speak(text, gender, speed)
elif command == "sts":
    text = stt()
    gender = int(input("Enter the gender of the voice (0 = male/ 2 =female): "))
    speed = input("Enter the speed of the voice (slow ,normal ,fast): ")
    speak(text, gender, speed)
elif command == "end":
    print("Exiting...")
else:
    print("Invalid command")
