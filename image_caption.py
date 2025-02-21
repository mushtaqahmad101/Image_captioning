import numpy as np
from PIL import Image
from transformers import AutoProcessor, BlipForConditionalGeneration
import torch

# Load the BLIP model and processor
processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")

def caption_image(input_image: np.ndarray):
    # Convert numpy array to PIL Image and convert to RGB
    raw_image = Image.fromarray(input_image).convert('RGB')

    # Process the image
    inputs = processor(images=raw_image, text="A picture of", return_tensors="pt")
    
    # Generate a caption
    with torch.no_grad():
        outputs = model.generate(**inputs, max_length=50)
    
    # Decode and return the caption
    caption = processor.decode(outputs[0], skip_special_tokens=True)
    return caption
