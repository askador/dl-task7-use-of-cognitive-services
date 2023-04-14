from http import client
from pathlib import Path
from google.cloud import speech
from google.cloud.speech_v1.types import RecognizeResponse
from environ import Env

env = Env()
env.read_env()

client = speech.SpeechClient.from_service_account_json(str(env('SPEECH_TO_TEXT_API_CREDENTIALS')))

def transcribe_audio(audio_file_path) -> RecognizeResponse:
    
    with open(audio_file_path, 'rb') as f:
        audio_file = f.read()
        
    audio = speech.RecognitionAudio(content=audio_file)
    
    config = speech.RecognitionConfig(
        enable_automatic_punctuation=True,
        language_code="en-US"
    )

    return client.recognize(config=config, audio=audio)
