# app/models/stable_diffusion.py
import uuid
import torch
from diffusers import StableDiffusionPipeline
from app.config import Config

def load_model(model_id, device="cpu", use_safetensors=False):
    """Load the Stable Diffusion model with specified configurations."""
    pipe = StableDiffusionPipeline.from_pretrained(
        model_id,
        torch_dtype=torch.float32 if device == "cpu" else torch.float16,
        use_safetensors=use_safetensors
    )
    return pipe.to(device)

# Load the model once during import to avoid reloading for each request
model_id = "dreamlike-art/dreamlike-diffusion-1.0"  # Replace with desired model ID
sd_model = load_model(model_id, device=Config.DEVICE)

def generate_image(prompt):
    """Generate an image using the Stable Diffusion model and save it to a file."""
    images = sd_model(prompt).images
    if not images:
        raise RuntimeError("No images generated")

    # Save the first generated image with a unique filename
    filename = f"{Config.IMAGE_OUTPUT_DIR}/generated_{uuid.uuid4()}.png"
    images[0].save(filename)
    return filename

