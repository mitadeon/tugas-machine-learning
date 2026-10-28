
from fastapi import FastAPI
from pydantic import BaseModel
import pandas as pd
import joblib

# Membuat aplikasi API
app = FastAPI(title="House Price Prediction API")

# Memuat model yang sudah dilatih
model = joblib.load("gbr_model.joblib")


@app.get("/")
def home():
    return {
        "message": "House Price Prediction API berhasil dijalankan"
    }


@app.post("/predict")
def predict(data: dict):
    # Mengubah data input menjadi DataFrame
    input_data = pd.DataFrame([data])

    # Melakukan prediksi harga rumah
    prediction = model.predict(input_data)

    return {
        "predicted_price": float(prediction[0])
    }
