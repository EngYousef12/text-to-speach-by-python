from flask import Flask, render_template, request, jsonify
import pyttsx3
import threading

app = Flask(__name__)

speed_rate = {"slow": 80, "normal": 200, "fast": 300}

def speak(text, speed, voice_gender):
    engine = pyttsx3.init()
    engine.setProperty("rate", speed_rate[speed])
    voices = engine.getProperty('voices')
    engine.setProperty("voice", voices[voice_gender].id)
    engine.say(text)
    engine.runAndWait()
    engine.stop()  # Ensure the engine stops after speaking

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/imitate', methods=['POST'])
def imitate_voice():
    data = request.json
    text = data['text']
    speed = data['speed']
    voice_gender = int(data['gender'])
    threading.Thread(target=speak, args=(text, speed, voice_gender)).start()
    return jsonify({'status': 'success'})

if __name__ == '__main__':
    app.run(debug=True)
