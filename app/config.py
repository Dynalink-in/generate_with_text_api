# app/config.py
import os
import torch

class Config:
    AUDIO_OUTPUT_DIR = "generated_audio"
    IMAGE_OUTPUT_DIR = "generated_images"
    DEVICE = "cuda" if torch.cuda.is_available() else "cpu"

# Ensure directories exist
os.makedirs(Config.AUDIO_OUTPUT_DIR, exist_ok=True)
os.makedirs(Config.IMAGE_OUTPUT_DIR, exist_ok=True)

