from fastapi import FastAPI
from pydantic import BaseModel
import joblib

class TextIn(BaseModel):
    text: str

class PredictionOut(BaseModel):
    emotion: str
    confidence: float

app = FastAPI()

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
