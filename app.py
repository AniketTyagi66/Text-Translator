from flask import Flask, render_template, request, redirect, url_for
from gtts import gTTS
import os
import speech_recognition as sr

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/converttospeech', methods=['POST'])
def converttospeech():
    if 'text' in request.form:  # Text to Speech conversion
        text = request.form['text']
        language = request.form['language']
        tts = gTTS(text, lang=language)
        tts.save('output.mp3')
        os.system('start output.mp3') # for Windows
        # os.system('mpg321 output.mp3') # for Linux

    return redirect(url_for('index'))


@app.route('/converttotext', methods=['POST'])
def converttotext():
    recognizer = sr.Recognizer()

    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio_data = recognizer.listen(source)
        print("Recording done.")

    try:
        text = recognizer.recognize_google(audio_data)
        return render_template('index.html', text=text)
    except sr.UnknownValueError:
        return "Error: Could not understand audio"
    except sr.RequestError as e:
        return f"Error: Could not request results; {e}"

if __name__ == '__main__':
    app.run(debug=True)
