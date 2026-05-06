# Traductor Español - Alemán

Aplicación web que traduce texto del español al alemán utilizando el modelo de lenguaje **Qwen2-0.5B-Instruct** de Alibaba Cloud. El modelo corre directamente en el navegador gracias a **Transformers.js**, sin necesidad de backend ni servidor.

**Demo en vivo:** [https://luislozanom.github.io/app_traductora/](https://luislozanom.github.io/app_traductora/)

## Uso online

Simplemente abre el enlace de arriba en tu navegador. La primera vez se descarga el modelo (~300 MB) y después queda en caché.

## Uso local (alternativa con Python)

También se incluye `app.py` para correr el modelo localmente con Flask:

```bash
git clone https://github.com/LuisLozanoM/app_traductora.git
cd app_traductora
pip install flask transformers torch
python app.py
```

Abrir en el navegador: **http://localhost:5000**

## Ejemplos incluidos

La interfaz incluye botones de acceso rápido con tres frases de prueba:

| Español              | Alemán esperado         |
|----------------------|-------------------------|
| Me gusta el fútbol   | Ich mag Fußball         |
| ¿Cómo estás?        | Wie geht es dir?        |
| ¿Qué hora es?       | Wie spät ist es?        |

## Estructura del proyecto

```
app_traductora/
├── app.py        # Backend Flask (alternativa local con Python)
├── index.html    # Frontend con Transformers.js (funciona en GitHub Pages)
└── README.md
```

## Modelo

Se utiliza [Qwen2.5-0.5B-Instruct](https://huggingface.co/onnx-community/Qwen2.5-0.5B-Instruct), un modelo de lenguaje de 0.5 mil millones de parámetros optimizado para seguir instrucciones, en formato ONNX cuantizado (q4) para ejecución en el navegador.

## Tecnologías

- **Frontend:** HTML, CSS, JavaScript (vanilla)
- **Modelo en navegador:** Transformers.js, ONNX Runtime Web
- **Backend local (opcional):** Python, Flask, Hugging Face Transformers, PyTorch
