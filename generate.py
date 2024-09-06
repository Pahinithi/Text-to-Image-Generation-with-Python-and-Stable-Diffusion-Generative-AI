from diffusers import DiffusionPipeline
import torch
from PIL import Image

# Check if MPS (Metal Performance Shaders) is available, otherwise fallback to CPU
if torch.backends.mps.is_available():
    device = "mps"
else:
    device = "cpu"

# Load the Stable Diffusion model and move it to the appropriate device
pipe = DiffusionPipeline.from_pretrained(
    "stabilityai/stable-diffusion-xl-base-1.0",
    torch_dtype=torch.float16 if device == "mps" else torch.float32,  # Use float16 for MPS, otherwise float32 for CPU
    use_safetensors=True,
    variant="fp16" if device == "mps" else None  # Set the variant to fp16 for MPS
)

pipe.to(device)

# Generate image and save it to a file
def generate_image(prompt: str, negative_prompt: str) -> str:
    # Generate the image
    images = pipe(prompt=prompt, negative_prompt=negative_prompt).images[0]
    
    # Save image to disk
    output_path = f"static/{prompt.replace(' ', '_')}.png"
    images.save(output_path)

    return output_path
