import streamlit as st
import requests

st.title("Iris Flower Prediction App")
sepal_length = st.number_input("Sepal Length (cm)") 
sepal_width = st.number_input("Sepal Width (cm)")
petal_length = st.number_input("Petal Length (cm)")
petal_width = st.number_input("Petal Width (cm)")

if st.button("Predict"):
    data = {
        "sepal_length": sepal_length,
        "sepal_width": sepal_width,
        "petal_length": petal_length,
        "petal_width": petal_width
    }
    response = requests.post("http://localhost:8000/predict", json=data)
    if response.status_code == 200:
        result = response.json()
        st.success(f"Predicted Class: {result['class_name']} (ID: {result['class_id']})")
    else:
        st.error("Error in prediction. Please try again.")