import streamlit as st
import numpy as np
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

# Load the CKD prediction model
model = RandomForestClassifier()
model.load_model('ckd_prediction_model.pkl')

# Define the user interface
st.title('CKD Prediction App')

# Get the user input
age = st.number_input('Age')
sex = st.selectbox('Sex', ['Male', 'Female'])
blood_pressure = st.number_input('Blood pressure (mmHg)')
serum_creatinine = st.number_input('Serum creatinine (mg/dL)')

# Make a prediction
prediction = model.predict_proba([
    [age, sex, blood_pressure, serum_creatinine]
])[0][1]

# Display the prediction
st.write('Probability of having CKD:', prediction)

# Provide feedback to the user
if prediction > 0.5:
    st.write('Your risk of having CKD is high. Please see a doctor for further evaluation.')
else:
    st.write('Your risk of having CKD is low. However, it is important to maintain a healthy lifestyle and get regular checkups to monitor your kidney function.')
