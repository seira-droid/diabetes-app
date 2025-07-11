import streamlit as st
import joblib

# Load model
model = joblib.load("diabetes_simplified.csv")

st.title("🩺  Diabetes Risk Predictor")

# Collect inputs
glucose = st.number_input("Glucose Level", min_value=0)
bmi = st.number_input("BMI", min_value=0.0)
age = st.number_input("Age", min_value=0)
bp = st.number_input("Blood Pressure", min_value=0)

# Predict
if st.button("Predict"):
    input_data = [[glucose, bmi, age, bp]]  # Must match model's expected shape

    try:
        prediction = model.predict(input_data)[0]
        probability = model.predict_proba(input_data)[0][1]

        st.subheader("Prediction Result:")
        if probability < 0.4:
            st.success(f"✅ Non-Diabetic (Risk Score: {probability:.2f})")
        elif probability < 0.7:
            st.warning(f"⚠️ Likely Diabetic (Risk Score: {probability:.2f})")
        else:
            st.error(f"❌ Diabetic (Risk Score: {probability:.2f})")

    except Exception as e:
        st.error("An error occurred during prediction.")
        st.write("Debug info:", str(e))




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
