import streamlit as st
import pickle
import numpy as np

# Load the trained model
with open('diabetes_model.pkl', 'rb') as f:
    model = pickle.load(f)

st.title("🩺 Diabetes Prediction App")

# Input fields
preg = st.number_input("Pregnancies", 0)
glucose = st.number_input("Glucose", 0)
bp = st.number_input("Blood Pressure", 0)
skin = st.number_input("Skin Thickness", 0)
insulin = st.number_input("Insulin", 0)
bmi = st.number_input("BMI", 0.0)
dpf = st.number_input("Diabetes Pedigree Function", 0.0)
age = st.number_input("Age", 0)

# Predict button
if st.button("Predict"):
    features = np.array([[preg, glucose, bp, skin, insulin, bmi, dpf, age]])
    prediction = model.predict(features)

    if prediction[0] == 1:
        st.error("🔴 Likely Diabetic")
    else:
        st.success("🟢 Not Diabetic")
