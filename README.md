🖼️ AI-Powered Text-to-Image Generator
Built using purely open-source models & frameworks

This project generates high-quality images from text prompts using Stable Diffusion and Hugging Face Diffusers.
It includes a Streamlit-based web UI, image saving, metadata logging, and prompt engineering features.

🚀 Project Overview

This system converts natural language descriptions into images using open-source text-to-image models.

The project demonstrates:

Generative AI model usage

Stable Diffusion pipelines

Prompt engineering techniques

Web-based user interface building

Local inference (CPU or GPU)

Image + metadata saving

🧠 Architecture
User → Streamlit UI → Text Prompt
     → pipeline.py (Stable Diffusion)
     → Model Inference (CPU/GPU)
     → Generated Images
     → Saved to outputs/images + metadata

Components:

app.py → UI & interaction

pipeline.py → Model loader + generator

Stable Diffusion v1.5 (open-source)

Diffusers → inference engine

Torch → model execution

PIL → image handling

🛠️ Technology Stack
Component	Technology
Model	Stable Diffusion 1.5 (open-source)
Framework	PyTorch
Pipeline	HuggingFace Diffusers
UI	Streamlit
Image Processing	Pillow
Metadata	JSON
Deployment	Local machine (CPU/GPU)
⚙️ Setup & Installation
1. Clone the Repo
git clone https://github.com/your-username/text-to-image-generator.git
cd text-to-image-generator

2. Create Virtual Environment
python -m venv venv
venv\Scripts\activate  # Windows
# OR
source venv/bin/activate  # Mac/Linux

3. Install Dependencies
pip install -r requirements.txt

🧩 Model Download Instructions

Stable Diffusion automatically downloads via Hugging Face:

Model used:
runwayml/stable-diffusion-v1-5

No manual download required.

🖥️ Hardware Requirements

✅ CPU Supported (slower)
→ 5–12 minutes per 512×512 image

✅ GPU Recommended
→ 1–5 seconds per image (8GB+ VRAM recommended)

Minimum:

8 GB RAM

Python 3.9+

Ideal:

NVIDIA GPU (RTX 2060/3060/4060 or better)

🎨 Usage Instructions
Run the app:
streamlit run app.py

UI Features:

Enter text prompt

Add negative prompt

Select number of images

Choose style (photorealistic, cartoon, etc.)

Adjust steps, size, guidance scale

View & download generated images

Metadata auto-saved

✍️ Example Prompts
Realistic:
a futuristic city at sunset, photorealistic, ultra-detailed, 4K

Artistic:
a robot painted in Van Gogh style, swirling brush strokes, vivid colors

Cartoon:
a cute cat riding a skateboard, cartoon, bold outlines

🔧 Prompt Engineering Tips
Improve quality:

Add:
highly detailed, 4K, ultra-sharp, dramatic lighting

Style enhancement:

photorealistic

oil painting

cyberpunk neon lights

Negative prompts:
blurry, lowres, bad anatomy, watermark, distorted

📁 Output Structure

Images saved in:

outputs/images/


Metadata saved in:

outputs/metadata/


Metadata example:

{
  "prompt": "a futuristic city at sunset",
  "steps": 25,
  "height": 512,
  "width": 512,
  "timestamp": "2025-11-29",
  "file": "outputs/images/xxxx.png"
}

🚧 Limitations

CPU generation is slow

Requires 8GB RAM minimum

Quality depends on prompt clarity

Not trained on private or custom datasets

🔮 Future Improvements

Add image upscaling (RealESRGAN)

Add custom training / LoRA fine-tuning

Add gallery page in UI

Add style-transfer using ControlNet

Add GPU container (Docker + CUDA)

📜 License

This project uses only open-source models (Stable Diffusion) under the CreativeML OpenRAIL-M License.