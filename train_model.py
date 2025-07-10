import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle

# Load correct dataset with 8 features
url = "https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv"
columns = ["Pregnancies", "Glucose", "BloodPressure", "SkinThickness", "Insulin",
           "BMI", "DiabetesPedigreeFunction", "Age", "Outcome"]

df = pd.read_csv(url, header=None, names=columns)

# Features and labels
X = df.drop("Outcome", axis=1)
y = df["Outcome"]

# Train the model
model = RandomForestClassifier()
model.fit(X, y)

# Save the model
with open("diabetes_model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Model retrained and saved with 8 features.")
