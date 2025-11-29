import streamlit as st
from pipeline import TextToImageGenerator
from io import BytesIO

st.set_page_config(page_title="Text to Image", layout="wide")

st.title("🖼️ Open-Source Text-to-Image Generator")
st.write("Generate images from text using Stable Diffusion.")

# Sidebar controls
st.sidebar.header("⚙️ Generation Settings")

num_images = st.sidebar.slider("Number of Images", 1, 4, 1)
guidance_scale = st.sidebar.slider("Guidance Scale", 1.0, 20.0, 7.5)
steps = st.sidebar.slider("Inference Steps", 10, 50, 25)
height = st.sidebar.selectbox("Height", [384, 448, 512], index=2)
width = st.sidebar.selectbox("Width", [384, 448, 512], index=2)
seed = st.sidebar.text_input("Seed (optional):", "")

style = st.sidebar.selectbox("Style", [
    "none", "photorealistic", "cartoon", "oil painting", "cyberpunk", "Van Gogh style"
])

# Main input
prompt = st.text_area("Enter your prompt:", "A futuristic city at sunset, highly detailed, 4K")
negative_prompt = st.text_area("Negative prompt (optional):", "blurry, low-quality, watermark")

# Style mappings
style_prompts = {
    "photorealistic": "photorealistic, ultra-detailed, 35mm lens",
    "cartoon": "cartoon style, bold outlines, colorful",
    "oil painting": "oil painting, canvas texture, brush strokes",
    "cyberpunk": "cyberpunk neon lighting, futuristic city",
    "Van Gogh style": "in the style of Van Gogh, swirling strokes"
}

if style != "none":
    prompt = f"{prompt}, {style_prompts[style]}"

generator = TextToImageGenerator()

# THE BUTTON (This MUST show)
generate_btn = st.button("🚀 Generate Image(s)")

# When clicked
if generate_btn:
    st.write("🔄 Generating... please wait...")

    seed_val = int(seed) if seed.isdigit() else None

    images, metadata_files = generator.generate(
        prompt=prompt,
        negative_prompt=negative_prompt,
        num_images=num_images,
        guidance_scale=guidance_scale,
        steps=steps,
        height=height,
        width=width,
        seed=seed_val
    )

    st.success("🎉 Done!")

    for idx, img in enumerate(images):
        st.image(img, caption=f"Image {idx+1}", use_column_width=True)

        # Download option
        buf = BytesIO()
        img.save(buf, format="PNG")
        st.download_button(
            label=f"Download Image {idx+1}",
            data=buf.getvalue(),
            file_name=f"image_{idx+1}.png",
            mime="image/png"
        )
