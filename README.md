# Mood Mirror

Mood Mirror es una aplicación web que analiza las emociones presentes en un texto usando un modelo de procesamiento de lenguaje natural. El backend está construido con FastAPI y sirve un punto de predicción `/predict`, mientras que el frontend es una página estática (HTML/CSS/JS) que consume la API y muestra los resultados con imágenes de emojis.

## Características

- Detección de emoción: alegría, tristeza, enojo, miedo, amor, sorpresa.
- Porcentaje de confiabilidad de la predicción.
- Frontend ligero con Tailwind CSS y DaisyUI.
- Servido como archivos estáticos desde FastAPI.

## Instalación

1. Clona el repositorio:

   ```bash
   git clone <url-del-repositorio>
   cd mood-mirror
   ```

2. Crea un entorno virtual e instala dependencias:
   ```bash
   python -m venv .venv
   source .venv/Scripts/activate  # Windows
   pip install --upgrade pip
   pip install -r requirements.txt
   ```

## Uso

1. Inicia el servidor de FastAPI:

   ```bash
   uvicorn api:app --reload
   ```

2. Abre tu navegador web e ingresa a `http://localhost:8000/`.

3. Ingresa un texto en inglés y haz clic en **Analizar**. Verás la emoción detectada y su grado de confianza.

## API

- **POST** `/predict`

  - Request Body: `{ "text": "Tu texto aquí" }`
  - Response: `{ "emotion": "joy", "confidence": 0.85 }`

- **GET** `/` sirve la página estática `index.html`.

## Entrenamiento del modelo

El notebook en `train/main.ipynb` muestra cómo entrenar el modelo de emociones y generar los archivos `.pkl`. Sólo es necesario si deseas actualizar o mejorar el modelo.
