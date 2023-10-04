import streamlit as st
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from joblib import dump, load

# Load the kidney disease dataset (make sure you have the dataset)
data = pd.read_csv("kidney_disease.csv")

# Preprocess the dataset (you may need to handle missing data, encode categorical variables, etc.)

# Split the data into features (X) and target (y)
X = data.drop(columns=['class'])
y = data['class']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train a machine learning model (Random Forest in this example)
clf = RandomForestClassifier(n_estimators=100)
clf.fit(X_train, y_train)

# Save the trained model
dump(clf, 'kidney_disease_model.joblib')

# Load the trained model
model = load('kidney_disease_model.joblib')

# Streamlit app
st.title("Chronic Kidney Disease Prediction")

# Sidebar for user input
st.sidebar.header("User Input")
age = st.sidebar.number_input("Age", min_value=0, max_value=120)
bp = st.sidebar.number_input("Blood Pressure (mm Hg)", min_value=0)
sg = st.sidebar.number_input("Specific Gravity", min_value=1.0, max_value=1.025)
al = st.sidebar.number_input("Albumin", min_value=0, max_value=5)
su = st.sidebar.number_input("Sugar", min_value=0, max_value=5)
rbc = st.sidebar.selectbox("Red Blood Cells", ['normal', 'abnormal'])
# Add more input fields for other features as needed

# Create a feature vector from user inputs
user_input = [age, bp, sg, al, su, rbc]  # Add more feature values as needed

# Predict using the trained model
if st.sidebar.button("Predict"):
    prediction = model.predict([user_input])
    st.write("Prediction Result:")
    if prediction[0] == 'ckd':
        st.write("You may have Chronic Kidney Disease (CKD).")
    else:
        st.write("You may not have Chronic Kidney Disease.")
