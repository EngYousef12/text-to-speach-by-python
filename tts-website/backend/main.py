
from text_to_speech import speak
from flask import Flask, render_template
import pyttsx3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)
