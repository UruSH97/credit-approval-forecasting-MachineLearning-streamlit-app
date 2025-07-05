import streamlit as st
import numpy as np
import joblib

# Load trained model and scaler
model = joblib.load('credit_model.pkl')
scaler = joblib.load('scaler.pkl')

# Title
st.title("Credit Card Approval Prediction App")
st.markdown("Enter applicant details below:")

# Input fields (update based on your final features)
Income = st.number_input("Income", min_value=0.0)
CreditScore = st.number_input("Credit Score", min_value=0.0)
DebtLog = st.number_input("Debt (log-transformed)", min_value=0.0)
Age = st.number_input("Age", min_value=18, max_value=100)
YearsEmployed = st.number_input("Years Employed", min_value=0.0)
Employed = st.selectbox("Employed?", [0, 1])
PriorDefault = st.selectbox("Prior Default?", [0, 1])
Citizen = st.selectbox("Citizenship Status", [0, 1, 2])  # Update as per encoding
Ethnicity = st.selectbox("Ethnicity", [0, 1, 2,3,4,5,6,7,8])         # Update as per encoding
EducationLevel = st.selectbox("Education Level", [0, 1, 2,3,4,5,6,7,8,9,10,11,12,13])  # Update as per encoding
BankCustomer = st.selectbox("Bank Customer?", [0, 1,2])
Married = st.selectbox("Marital Status", [0, 1, 2])  
Male = st.selectbox("Gender", [0, 1])
IncomeLog = np.log1p(Income)
CreditScoreLog = np.log1p(CreditScore)
DebtLog = np.log1p(DebtLog)  # Assuming DebtLog is already log-transformed

# Button
if st.button("Predict Approval"):
    input_data = np.array([[Income, CreditScore, DebtLog, Age, YearsEmployed, Employed, PriorDefault,
                            Citizen, Ethnicity, EducationLevel, BankCustomer, Married, Male, IncomeLog, CreditScoreLog, DebtLog]])
    
    # Scale input
    input_scaled = scaler.transform(input_data)
    
    # Predict
    prediction = model.predict(input_scaled)
    
    # Output
    if prediction[0] == 1:
        st.success("✅ Application Approved!")
    else:
        st.error("❌ Application Denied.")
