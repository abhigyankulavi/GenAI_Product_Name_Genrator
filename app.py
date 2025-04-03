import gradio as gr
from transformers import T5Tokenizer, T5ForConditionalGeneration

model_path = "t5_product_name_generator" 
tokenizer = T5Tokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path)


def generate_names(description, tone, num_names=1):
    if not description or not tone:
        return ["Error: Product description and tone are required!"]
    
    input_text = f"Describe: {description} | Tone: {tone}"
    input_ids = tokenizer(input_text, return_tensors="pt").input_ids
    
    outputs = model.generate(
        input_ids, 
        max_length=32, 
        num_return_sequences=int(num_names), 
        do_sample=True, 
        top_k=50, 
        top_p=0.95
    )

    return [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

demo = gr.Interface(
    fn=generate_names, 
    inputs=[
        gr.Textbox(label="Product Description", placeholder="Enter product details..."),
        gr.Textbox(label="Brand Tone", placeholder="Enter brand personality..."),
        gr.Slider(1, 10, value=3, step=1, label="Number of Names")
    ],
    outputs=gr.Textbox(label="Generated Product Names"),
    title="AI Product Name Generator",
    description="Generate catchy product names based on description and brand tone.",
    theme="default"
)

# Launch the app
demo.launch()
