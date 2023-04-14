from flask import request, jsonify
from datetime import datetime
from app import app
import uuid
from pathlib import Path
from utils import update_reviews
from speech_to_text import transcribe_audio

AUDIO_FILES_PATH = Path(__file__).parent.parent.joinpath('./audios')

@app.route('/voice', methods=["POST"])
def voice():
    if not ('voice' in request.files.keys()):
        return jsonify({'errorMessage': 'Please provide a "voice" file'}), 400
    if not request.form.get('hotelId'):
        return jsonify({'errorMessage': 'Your request must contain "hotelId" value'}), 400
    
    audio = request.files['voice']
    file_extension = str(audio.filename).split('.')[-1]
    file_id = uuid.uuid4()
    file_name = f'{file_id}.{file_extension}'
    file_path = AUDIO_FILES_PATH.joinpath(file_name) 
    audio.save(file_path)
    
    transcribed_audio_resp = transcribe_audio(file_path)
    transcript = transcribed_audio_resp.results[0].alternatives[0].transcript
    
    update_reviews(request.form.get('hotelId'), {
        "date": datetime.now().isoformat(),
        "audioId": file_name,
        "text": transcript
    })
    
    return jsonify({'message': 'Done'}), 200
    