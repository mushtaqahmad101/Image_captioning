import gradio as gr
from image_caption import caption_image

dice = gr.Interface(
    fn=caption_image,
    inputs=gr.Image(),
    outputs="text",
    title="Image Captioning",
    description="Upload an image and get a beautiful caption!"
)

dice.launch(share=True)