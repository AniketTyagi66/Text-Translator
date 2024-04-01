from flask import Flask, render_template, request, redirect, url_for
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert():
    text = request.form['text']
    language = request.form['language']
    tts = gTTS(text, lang=language)
    tts.save('output.mp3')
    os.system('start output.mp3') # for Windows
    # os.system('mpg321 output.mp3') # for Linux
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
