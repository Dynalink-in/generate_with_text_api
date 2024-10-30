# app/models/minicpm.py
from transformers import AutoModelForCausalLM, AutoTokenizer
from app.config import Config

device = Config.DEVICE
model_name = "OpenAssistant/minicpm-2b"
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForCausalLM.from_pretrained(
    model_name,
    torch_dtype=torch.float16 if device == "cuda" else torch.float32
).to(device)

def process_multimodal(text):
    """Process text using MinICPM"""
    inputs = tokenizer(text, return_tensors="pt").to(device)
    outputs = model.generate(
        **inputs,
        max_length=100,
        num_return_sequences=1,
        temperature=0.7,
        do_sample=True
    )
    response = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return response

