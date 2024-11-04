import speech_recognition as sr

r = sr.Recognizer()

def speech_to_text():
    r = sr.Recognizer()
    while(1):
        try:
            with sr.Microphone() as source:
                r.adjust_for_ambient_noise(source, duration=0.3)
                print("start talking")
                audio = r.listen(source)
                MyText = r.recognize_google(audio)
                return MyText

        except sr.RequestError as e:
            print("Could not request results {0}".format(e))

        except sr.UnknownValueError:
            print("unknown error occurred")
    return

def output_text(text):
    f = open("output.txt", "a")
    f.write(text)
    f.write("\n")
    f.close()
    return

if __name__ == "__main__":
    text = ""
    while(text!="stop"):
        text = speech_to_text()
        output_text(text)

        print(text)
