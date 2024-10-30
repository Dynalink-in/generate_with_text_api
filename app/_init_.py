# app/__init__.py
from flask import Flask
from app.routes.image_routes import image_bp
from app.routes.speech_routes import speech_bp
from app.routes.multimodal_routes import multimodal_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(image_bp, url_prefix='/api')
    app.register_blueprint(speech_bp, url_prefix='/api')
    app.register_blueprint(multimodal_bp, url_prefix='/api')
    return app

