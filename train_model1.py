import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
import seaborn as sn
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.ensemble import AdaBoostClassifier
from sklearn.metrics import accuracy_score,confusion_matrix,classification_report
import pickle

url ="/content/drive/MyDrive/dataset/diabetes.csv"

columns = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin",
           "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"]
data = pd.read_csv(url, header=None, names=columns)




data.shape
data.dtypes
data.isna().sum()
x=data.drop(['Outcome'],axis=1)
y=data['Outcome']
x_train,x_test,y_train,y_test=train_test_split(x,y,test_size=0.2,random_state=5)

model=AdaBoostClassifier()
model.fit(x_train,y_train)
pred_y=model.predict(x_test)
pred_y

with open("diabetes_model", "wb") as f:
    pickle.dump(model, f)

print("✅ Model trained and saved with 8 features.")



import streamlit as st

def diabetes_bot(user_input):
    user_input = user_input.lower()
    if "bmi" in user_input:
        return "BMI is calculated as weight (kg) divided by height (m) squared. You can use our BMI calculator below!"
    elif "diabetes" in user_input:
        return "Diabetes is a condition where the body can't regulate blood sugar properly."
    else:
        return "I'm still learning! Try asking about diabetes or BMI."

st.subheader("🤖 Ask the Diabetes Bot")
user_q = st.text_input("Type your question here")
if user_q:
    st.markdown(f"**You:** {user_q}")
    response = diabetes_bot(user_q)
    st.markdown(f"**Bot:** {response}")


    

    st.subheader("🧮 BMI Calculator")
weight = st.number_input("Enter your weight (kg):", min_value=10.0, max_value=200.0, step=0.1)
height = st.number_input("Enter your height (cm):", min_value=50.0, max_value=250.0, step=0.1)

if weight and height:
    height_m = height / 100
    bmi = weight / (height_m ** 2)
    st.markdown(f"**Your BMI is:** `{bmi:.2f}`")

    if bmi < 18.5:
        st.info("You are underweight.")
    elif bmi < 25:
        st.success("You have a normal weight.")
    elif bmi < 30:
        st.warning("You are overweight.")
    else:
        st.error("You are obese.")


st.subheader("💡 Health Tips")
st.markdown("""
- Eat a balanced, low-sugar diet.
- Get regular exercise (30 mins a day).
- Avoid smoking and excessive alcohol.
- Get blood sugar checked regularly.
""")


