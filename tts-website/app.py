
from flask import Flask, render_template
import pyttsx3

speed_to_rate = {"slow" : 80, "normal" : 200, "fast" : 300}

def speak(text, gender ,speed):
    engine = pyttsx3.init()
    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[gender].id)
    engine.setProperty('rate', speed_to_rate[speed])
    engine.say(text)
    engine.runAndWait()
    engine.stop()

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
