from flask import Flask, request, jsonify, send_file
from transformers import AutoModelForCausalLM, AutoTokenizer
import torch

app = Flask(__name__)

MODEL_NAME = "Qwen/Qwen2-0.5B-Instruct"

print("Cargando modelo Qwen2-0.5B-Instruct...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForCausalLM.from_pretrained(MODEL_NAME)
model.eval()
print("Modelo cargado exitosamente.")


@app.route("/")
def index():
    return send_file("index.html")


@app.route("/traducir", methods=["POST"])
def traducir():
    data = request.json
    texto = data.get("texto", "").strip()

    if not texto:
        return jsonify({"traduccion": ""})

    prompt_sistema = (
        "You are a professional Spanish-to-German translator. "
        "Translate the user's Spanish text into German. "
        "Reply ONLY with the German translation. No explanations, no extra text.\n\n"
        "Examples:\n"
        "Spanish: Buenos días → German: Guten Morgen\n"
        "Spanish: Gracias → German: Danke\n"
        "Spanish: ¿Dónde está la biblioteca? → German: Wo ist die Bibliothek?"
    )

    messages = [
        {"role": "system", "content": prompt_sistema},
        {"role": "user", "content": texto},
    ]

    input_text = tokenizer.apply_chat_template(
        messages, tokenize=False, add_generation_prompt=True
    )
    inputs = tokenizer(input_text, return_tensors="pt").to(model.device)

    with torch.no_grad():
        outputs = model.generate(
            **inputs,
            max_new_tokens=128,
            temperature=0.3,
            do_sample=True,
            top_p=0.9,
            repetition_penalty=1.2,
        )

    respuesta = tokenizer.decode(
        outputs[0][inputs["input_ids"].shape[1] :], skip_special_tokens=True
    )

    return jsonify({"traduccion": respuesta.strip()})


if __name__ == "__main__":
    print("Servidor iniciado en http://localhost:5000")
    app.run(debug=False, port=5000)
