from fastapi import FastAPI
from pydantic import BaseModel
import joblib
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    emotion: str
    confidence: float

app = FastAPI()
app.mount(
    "/static/assets/emoji",
    StaticFiles(directory="static/assets/emoij"),
    name="emoji_alias"
)
app.mount("/static", StaticFiles(directory="static"), name="static")

model = joblib.load("models/emotion_model.pkl")
tfidf = joblib.load("models/tfidf_vectorizer.pkl")

@app.post("/predict", response_model=PredictionOut)
def predict_emotion(payload: TextIn):
    X = tfidf.transform([payload.text])
    probs = model.predict_proba(X)[0]
    idx = probs.argmax()
    emotion = model.classes_[idx]
    confidence = float(probs[idx])
    return PredictionOut(emotion=emotion, confidence=confidence)

@app.get("/", response_class=FileResponse)
def serve_index():
    return FileResponse("static/index.html")
