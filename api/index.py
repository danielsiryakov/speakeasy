from flask import Flask
import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

app = Flask(__name__)

@app.route('/')
def home():
    print(os.getcwd())
    return 'Hello, World!'

@app.route('/about')
def about():
    audio_file = open("./api/sample1.mp3", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    print(transcript)
    return transcript.to_dict()