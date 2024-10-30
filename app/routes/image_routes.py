# app/routes/image_routes.py
from flask import Blueprint, request, jsonify, send_file
from app.models.stable_diffusion import generate_image

image_bp = Blueprint('image', __name__)

@image_bp.route('/generate-image', methods=['POST'])
def image_endpoint():
    data = request.get_json()
    if not data or 'prompt' not in data:
        return jsonify({'error': 'No prompt provided'}), 400
    image_path = generate_image(data['prompt'])
    return send_file(image_path, mimetype='image/png')

