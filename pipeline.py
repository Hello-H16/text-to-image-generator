# pipeline.py
import torch
from diffusers import StableDiffusionPipeline, DPMSolverMultistepScheduler
from PIL import Image
import os
import uuid
from datetime import datetime
import json

# Output folders
OUTPUT_IMAGES = "outputs/images"
OUTPUT_METADATA = "outputs/metadata"
os.makedirs(OUTPUT_IMAGES, exist_ok=True)
os.makedirs(OUTPUT_METADATA, exist_ok=True)


class TextToImageGenerator:
    def __init__(self, model_id="runwayml/stable-diffusion-v1-5", device=None):
        self.model_id = model_id

        # Detect device
        if device:
            self.device = device
        else:
            self.device = "cuda" if torch.cuda.is_available() else "cpu"

        # Load the pipeline
        self.pipe = StableDiffusionPipeline.from_pretrained(
            model_id,
            torch_dtype=torch.float32,   # CPU friendly
            safety_checker=None          # Remove unnecessary checks for open-source
        )

        # Use CPU
        self.pipe = self.pipe.to(self.device)

        # Faster scheduler
        self.pipe.scheduler = DPMSolverMultistepScheduler.from_config(self.pipe.scheduler.config)

    def generate(
        self,
        prompt,
        negative_prompt="",
        num_images=1,
        guidance_scale=7.5,
        steps=25,
        height=512,
        width=512,
        seed=None
    ):
        # Seed setup
        generator = None
        if seed is not None:
            generator = torch.Generator("cpu").manual_seed(seed)

        # Run model
        result = self.pipe(
            prompt=[prompt] * num_images,
            negative_prompt=[negative_prompt] * num_images if negative_prompt else None,
            guidance_scale=guidance_scale,
            num_inference_steps=steps,
            height=height,
            width=width,
            generator=generator
        )

        images = result.images  # list of PIL images
        metadata_paths = []

        for i, img in enumerate(images):
            file_id = uuid.uuid4().hex[:8]
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{timestamp}_{file_id}"

            # Save PNG
            img_path = os.path.join(OUTPUT_IMAGES, f"{filename}.png")
            img.save(img_path)

            # Save metadata
            metadata = {
                "prompt": prompt,
                "negative_prompt": negative_prompt,
                "guidance_scale": guidance_scale,
                "steps": steps,
                "height": height,
                "width": width,
                "seed": seed,
                "timestamp": timestamp,
                "file": img_path
            }

            meta_path = os.path.join(OUTPUT_METADATA, f"{filename}.json")
            with open(meta_path, "w") as f:
                json.dump(metadata, f, indent=4)
