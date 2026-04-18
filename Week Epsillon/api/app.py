import streamlit as st
import requests

st.set_page_config(page_title="Iris Classifier 🌸", layout="centered")

st.title("🌸 Iris Flower Prediction")
st.write("Enter the flower measurements below and predict the species!")

# Input sliders
sepal_length = st.slider("Sepal Length", 4.0, 8.0, 5.4)
sepal_width = st.slider("Sepal Width", 2.0, 4.5, 3.4)
petal_length = st.slider("Petal Length", 1.0, 7.0, 1.3)
petal_width = st.slider("Petal Width", 0.1, 2.5, 0.2)

# Predict button
if st.button("Predict 🌿"):
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/predict",
            json=data
        )

        if response.status_code == 200:
            result = response.json()
            st.success(f"Prediction: {result['class_name']} 🌼")
            st.write(f"Class ID: {result['class_id']}")
        else:
            st.error("API error 😢")

    except Exception as e:
        st.error("Could not connect to FastAPI server")