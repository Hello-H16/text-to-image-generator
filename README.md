<p align="center">
  <img src="assets/banner.png" width="100%">
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Project-AI%20%2F%20Generative%20Model-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Framework-Streamlit-red?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Model-Stable%20Diffusion%201.5-green?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Library-Diffusers-yellow?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Python-3.9+-blue?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active-success?style=for-the-badge" />
</p>

# 🖼️ Text-to-Image Generator (Stable Diffusion 1.5)
A fully **open-source text-to-image generator** built using **Stable Diffusion**, **PyTorch**, and a clean **Streamlit UI**.  
Supports **CPU and GPU**, prompt engineering, negative prompts, style presets, and metadata storage.

---

# 🔥 Features

### 🧠 AI Model  
- Stable Diffusion 1.5 (open-source)  
- Diffusers pipeline (HuggingFace)  
- Works on **CPU fallback** and **GPU if available**

### 🎨 Generation  
- Text prompts  
- Negative prompts  
- Style presets (Photorealistic, Cartoon, Cyberpunk, Van Gogh)  
- Multiple image generation  
- Adjustable steps, guidance scale, resolution  
- Metadata saved automatically

### 🌐 Web UI  
- Built with Streamlit  
- Easy-to-use interface  
- Download generated images  
- Simple sliders + dropdown controls  

---

# 📁 Folder Structure

text-to-image-generator/
│── app.py # Streamlit UI
│── pipeline.py # Backend: Stable Diffusion generation
│── requirements.txt # Dependencies
│── README.md
│
│── utils/
│ └── prompt_engineering.md # Prompt engineering guide
│
│── outputs/
│ ├── images/ # Generated images
│ └── metadata/ # Metadata for each image
│
│── models/ # (Optional) Model storage
│
└── assets/
└── banner.png # Project banner


---

# 🧠 Research Topics (Required by Project)

### ✔ Generative Adversarial Networks (GANs)
- Generator vs discriminator  
- Why diffusion models outperform GANs for image generation  

### ✔ Diffusion Models (Core of Stable Diffusion)
- Forward noise process  
- Reverse denoising  
- Latent Diffusion Models (LDM)  
- U-Net architecture  
- CLIP text encoder  

### ✔ Prompt Engineering  
- Positive and negative prompts  
- Style conditioning  
- Quality boost keywords  
- Avoiding artifacts  

---

# 🚀 Installation & Setup

### 1️⃣ Clone the repository  
```bash
git clone https://github.com/Hello-H16/text-to-image-generator.git
cd text-to-image-generator
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate    # Windows
# OR
source venv/bin/activate # Mac/Linux

3️⃣ Install Dependencies
pip install -r requirements.txt

⚡ Hardware Support
🔥 GPU (Preferred)

If using NVIDIA GPU, install CUDA-enabled PyTorch:

pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu118


Benefits:

10× faster

FP16 inference

Larger image sizes

🧠 CPU (Fallback)

Stable Diffusion runs fully on CPU:

384×384 image → ~5–12 minutes

512×512 → slower

Recommended settings:

Steps: 20–25

Size: 384×384

Guidance: 6–8

No GPU required.

🖥️ Running the App
streamlit run app.py


The app will open in your browser at:

http://localhost:8501

🎨 Sample Outputs

(Add your sample images after first generation)

<p align="center">
  <img src="samples/sample1.png" width="45%">
  <img src="samples/sample2.png" width="45%">
</p>

📦 Metadata Example

Each generated image saves metadata:

{
  "prompt": "a futuristic city at sunset",
  "negative_prompt": "blurry",
  "steps": 25,
  "guidance_scale": 7.5,
  "height": 512,
  "width": 512,
  "timestamp": "2025-03-01_134522",
  "file": "outputs/images/20250301_134522.png"
}

🧪 Prompt Engineering Guide

See:
👉 utils/prompt_engineering.md

🚧 Limitations

CPU generation is slow

Requires internet for model download (first time)

4GB+ model size

More GPU = better performance

🔮 Future Improvements

ControlNet support

Real-ESRGAN upscaling

LoRA fine-tuning

Gallery view in UI

Style mixing slider

📝 License

This project uses Stable Diffusion under the CreativeML OpenRAIL-M License.

<p align="center"> Made with ❤️ by <b>Hemant Shetty</b> </p> ```