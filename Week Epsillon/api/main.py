from fastapi import FastAPI
import joblib
import os

from src.schema import Iris

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
model_path = os.path.join(BASE_DIR, "src", "iris_model.pkl")

model = joblib.load(model_path)
labels = ["setosa", "versicolor", "virginica"]

@app.get('/')
def home():
    return {"message": "Welcome to the Iris Prediction API"}

@app.post('/predict')
def predict(data: Iris):
    features = [
        data.sepal_length,
        data.sepal_width,
        data.petal_length,
        data.petal_width
    ]
    prediction = model.predict([features])[0]
    return {
        "class_id": int(prediction),
        "class_name": labels[prediction]
    }