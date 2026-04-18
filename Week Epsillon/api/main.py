from fastapi import FastAPI
import joblib
import os

from src.schema import Iris

app = FastAPI()

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
print(BASE_DIR)
model_path = os.path.join(BASE_DIR, "src", "iris_model.pkl")
print(model_path)
model = joblib.load(model_path)
print("Model loaded successfully")
labels = ["setosa", "versicolor", "virginica"]
print("Labels defined successfully\n", labels)

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