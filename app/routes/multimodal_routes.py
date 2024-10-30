# app/routes/multimodal_routes.py
from flask import Blueprint, request, jsonify
from app.models.minicpm import process_multimodal

multimodal_bp = Blueprint('multimodal', __name__)

@multimodal_bp.route('/process-text', methods=['POST'])
def multimodal_endpoint():
    data = request.get_json()
    if not data or 'text' not in data:
        return jsonify({'error': 'No text provided'}), 400
    response = process_multimodal(data['text'])
    return jsonify({'response': response})

