# Traductor Español - Alemán

Aplicación web que traduce texto del español al alemán utilizando el modelo de lenguaje **Qwen2-0.5B-Instruct** de Alibaba Cloud. El backend carga el modelo localmente con la librería `transformers` de Hugging Face y lo expone a través de un servidor Flask, mientras que el frontend es una interfaz HTML interactiva.

## Requisitos

- Python 3.10+
- pip

### Dependencias

```
flask
transformers
torch
```

## Instalación

```bash
git clone https://github.com/LuisLozanoM/app_traductora.git
cd app_traductora
pip install flask transformers torch
```

## Uso

1. Ejecutar el servidor:

```bash
python app.py
```

2. Abrir en el navegador: **http://localhost:5000**

3. Escribir cualquier texto en español en el campo de entrada y presionar **Traducir** (o Enter).

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
├── app.py        # Backend Flask + carga del modelo Qwen2-0.5B-Instruct
├── index.html    # Frontend con la interfaz de traducción
└── README.md
```

## Modelo

Se utiliza [Qwen2-0.5B-Instruct](https://huggingface.co/Qwen/Qwen2-0.5B-Instruct), un modelo de lenguaje de 0.5 mil millones de parámetros optimizado para seguir instrucciones. La primera ejecución descarga el modelo automáticamente desde Hugging Face (~1 GB).

## Tecnologías

- **Backend:** Python, Flask, Hugging Face Transformers, PyTorch
- **Frontend:** HTML, CSS, JavaScript (vanilla)
- **Modelo:** Qwen2-0.5B-Instruct
