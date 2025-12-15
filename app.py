import streamlit as st
import pickle
import numpy as np

# 1. Configure the page
st.set_page_config(page_title="Blood Pressure Predictor")

# 2. Add Title and Description
st.title("BMI to Systolic Blood Pressure Predictor")
st.write("Enter a BMI value below to predict the Systolic Blood Pressure using your trained Linear Regression model.")

# 3. Input Field for BMI
# We set a reasonable range for BMI (e.g., 10 to 60)
bmi_input = st.number_input("Enter BMI Value:", min_value=10.0, max_value=60.0, value=25.0, step=0.1)

# 4. Load the trained model
try:
    # Ensure this matches the filename you uploaded exactly
    with open('bmi_systolic_bp_model.pkl', 'rb') as file:
        model = pickle.load(file)

    # 5. Make Prediction
    if st.button("Predict"):
        # The model expects a 2D array input like [[value]]
        prediction = model.predict([[bmi_input]])
        
        # Display the result
        st.success(f"Predicted Systolic Blood Pressure: {prediction[0]:.2f} mmHg")

except FileNotFoundError:
    st.error("Error: The file 'bmi_systolic_bp_model.pkl' was not found. Please verify it is uploaded to your GitHub repository.")
  
