# model.py
import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load dataset
data = pd.read_csv("diabetes.csv")  # Your CSV with at least glucose, bmi, age, bp, outcome

# Select 4 features
X = data[["Glucose", "BMI", "Age", "BloodPressure"]]
y = data["Outcome"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
joblib.dump(model, "diabetes_model.pkl")
print("✅ Model trained and saved with 4 features.")
