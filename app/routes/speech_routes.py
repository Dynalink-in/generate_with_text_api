# app/routes/speech_routes.py
from flask import Blueprint, request, jsonify, send_file
from app.models.coqui_tts import generate_speech

speech_bp = Blueprint('speech', __name__)

@speech_bp.route('/generate-speech', methods=['POST'])
def speech_endpoint():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    audio_path = generate_speech(data['text'], data.get('speaker_id'))
    return send_file(audio_path, mimetype='audio/wav')

