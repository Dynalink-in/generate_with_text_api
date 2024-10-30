# app/models/stable_diffusion.py
from diffusers import StableDiffusionPipeline
from app.config import Config

device = Config.DEVICE
sd_model = StableDiffusionPipeline.from_pretrained(
    "runwayml/stable-diffusion-v1-5",
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
).to(device)

def generate_image(prompt):
    """Generate image using Stable Diffusion"""
    image = sd_model(prompt).images[0]
    filename = f"{Config.IMAGE_OUTPUT_DIR}/generated_{uuid.uuid4()}.png"
    image.save(filename)
    return filename

