import gradio as gr
from transformers import T5Tokenizer, T5ForConditionalGeneration

model_path = "./"
tokenizer = T5Tokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path)

def generate_names(description, tone, num_names):
    if not description or not tone:
        return [" Error: Product description and tone are required!"]
    
    input_text = f"Generate product names for: {description} with a {tone} brand tone."

    input_ids = tokenizer(input_text, return_tensors="pt").input_ids

    outputs = model.generate(
        input_ids, 
        max_length=32, 
        num_return_sequences=int(num_names), 
        do_sample=True, 
        top_k=50, 
        top_p=0.95
    )

    formatted_names = [f" {i+1}. {tokenizer.decode(output, skip_special_tokens=True).strip()}" for i, output in enumerate(outputs)]
    return "\n".join(formatted_names)

demo = gr.Interface(
    fn=generate_names, 
    inputs=[
        gr.Textbox(label="Product Description", placeholder="Enter product details..."),
        gr.Textbox(label="Brand Tone", placeholder="Enter brand personality..."),
        gr.Slider(1, 10, value=3, step=1, label="Number of Names")
    ],
    outputs=gr.Textbox(label="Generated Product Names", lines=10),
    title=" AI Product Name Generator ",
    description=" Generate catchy product names based on description and brand tone!",
    theme="default"
)

demo.launch()
