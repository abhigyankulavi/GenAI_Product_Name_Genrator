from flask import Flask, request, jsonify
from transformers import T5Tokenizer, T5ForConditionalGeneration
import torch

app = Flask(__name__)

model_path = "t5_product_name_generator" 
tokenizer = T5Tokenizer.from_pretrained(model_path)
model = T5ForConditionalGeneration.from_pretrained(model_path)

@app.route("/generate", methods=["POST"])
def generate_product_names():
    try:
        data = request.json
        description = data.get("description", "").strip()
        tone = data.get("tone", "").strip()
        num_names = int(data.get("num_names", 1))

        if not description or not tone:
            return jsonify({"error": "Product description and tone are required!"}), 400

        input_text = f"Describe: {description} | Tone: {tone}"
        input_ids = tokenizer(input_text, return_tensors="pt").input_ids

        outputs = model.generate(input_ids, max_length=32, num_return_sequences=num_names, do_sample=True, top_k=50, top_p=0.95)
        product_names = [tokenizer.decode(output, skip_special_tokens=True) for output in outputs]

        return jsonify({"product_names": product_names})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
