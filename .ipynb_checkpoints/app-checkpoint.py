# import streamlit as st
# import joblib 
# import numpy as np

# st.title("House Price Prediction ")
# st.divider()

# st.write("This Webiste uses machine learning model for Prediciting house price with given features of the house. For using this website you can enter the inputs from this User Interface and then use predict button")

# st.divider()

# PRT_ID = st.number_inputs("Enter the PRT_ID",min_value=0,value=0)
# area = st.number_inputs("Enter the living Area ",min_value=0,value=0)
# bedrooms = st.number_inputs("Number of Bedroom",min_value=0,value=0)
# bathrooms = st.number_inputs("Number of Bathroom",min_value=0,value=0)

# st.divider()

# X =[[PRT_ID,area,bedrooms,bathrooms]]

# predictbutton = st.button("Predict")

# if predictbutton:
#     st.balloons()
#     X_array = np.array(X)
#     prediction = model.predict(X_array)
#     st.write(f"Price Prediction is {prediction}")
# else:
#     st.write("Please use predict button after entering value")

import streamlit as st
import joblib
import numpy as np
import pandas as pd
from datetime import date

# Load the trained model and the encoder/scaler if used during training
model = joblib.load('model.pkl')

# Title of the app
st.title("House Price Prediction")
st.divider()

# Description of the app
st.write("This website uses a machine learning model for predicting house prices based on given features. Enter the inputs from this user interface and then click the predict button.")

st.divider()

# Input fields for all 21 features
PRT_ID = st.text_input("PRT_ID (e.g., P0885)", value="P0001")
AREA = st.selectbox("AREA", options=["Chrompet", "Karapakkam", "Velachery", "Anna Nagar", "Adyar"])
INT_SQFT = st.number_input("Interior Square Footage", min_value=0.0, value=0.0)
DATE_SALE = st.date_input("Date of Sale", value=date.today())
N_BEDROOM = st.number_input("Number of Bedrooms", min_value=0, value=0)
N_BATHROOM = st.number_input("Number of Bathrooms", min_value=0, value=0)
SALE_COND = st.selectbox("Sale Condition", options=["Normal", "Abnormal", "Partial", "Alloca", "Family", "Other"])
PARK_FACIL = st.selectbox("Parking Facility", options=["Yes", "No"])
DATE_BUILD = st.date_input("Date Built", value=date.today())
BUILDTYPE = st.selectbox("Building Type", options=["Detached", "Semi-Detached", "Terraced", "Flat"])
UTILITY_AVAIL = st.selectbox("Utility Availability", options=["All", "NoSewr", "NoSeWa", "ELO", "NoWater"])
STREET = st.selectbox("Street Type", options=["Paved", "Gravel", "Dirt"])
MZZONE = st.selectbox("Zoning", options=["A", "B", "C", "D", "E"])
QS_ROOMS = st.number_input("Quality of Rooms", min_value=0, value=0)
QS_BATHROOM = st.number_input("Quality of Bathrooms", min_value=0, value=0)
QS_BEDROOM = st.number_input("Quality of Bedrooms", min_value=0, value=0)
QS_OVERALL = st.number_input("Overall Quality", min_value=0, value=0)
REG_FEE = st.number_input("Registration Fee", min_value=0.0, value=0.0)
COMMIS = st.number_input("Commission", min_value=0.0, value=0.0)
SALES_PRICE= st.number_input("Sales Agent price ", min_value=0.0, value=0.0)
Price_actual= st.number_input("Price Actual", min_value=0.0, value=0.0)

st.divider()

# Prepare the input data for prediction
input_data = pd.DataFrame([{
    "PRT_ID": PRT_ID,
    "AREA": AREA,
    "INT_SQFT": INT_SQFT,
    "DATE_SALE": DATE_SALE,
    "N_BEDROOM": N_BEDROOM,
    "N_BATHROOM": N_BATHROOM,
    "SALE_COND": SALE_COND,
    "PARK_FACIL": PARK_FACIL,
    "DATE_BUILD": DATE_BUILD,
    "BUILDTYPE": BUILDTYPE,
    "UTILITY_AVAIL": UTILITY_AVAIL,
    "STREET": STREET,
    "MZZONE": MZZONE,
    "QS_ROOMS": QS_ROOMS,
    "QS_BATHROOM": QS_BATHROOM,
    "QS_BEDROOM": QS_BEDROOM,
    "QS_OVERALL": QS_OVERALL,
    "REG_FEE": REG_FEE,
    "COMMIS": COMMIS
}])

# Apply the same preprocessing as was done during training
# Example: Convert categorical features to one-hot encoding
input_data_encoded = pd.get_dummies(input_data)

# Ensure the number of features matches the trained model's input
# Align columns (if the model was trained with specific column order)
# This step may need adjustment based on how the model was trained
input_data_encoded = input_data_encoded.reindex(columns=model.feature_names_in_, fill_value=0)

# Predict button
predict_button = st.button("Predict")

if predict_button:
    st.balloons()
    prediction = model.predict(input_data_encoded)
    
    # Display the prediction
    st.write(f"Price Prediction is: {prediction[0]:,.2f}")

else:
    st.write("Please enter the values and click the predict button.")
