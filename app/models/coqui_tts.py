# app/models/coqui_tts.py
from TTS.api import TTS
from app.config import Config
import uuid

device = Config.DEVICE
tts = TTS("tts_models/en/vctk/vits").to(device)

def generate_speech(text, speaker_id=None):
    """Generate speech using Coqui TTS"""
    filename = f"{Config.AUDIO_OUTPUT_DIR}/speech_{uuid.uuid4()}.wav"
    tts.tts_to_file(text=text, file_path=filename, speaker=speaker_id)
    return filename

