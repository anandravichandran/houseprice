import streamlit as st
import pickle
import numpy as np
import pandas as pd

# Load model and scaler
model = pickle.load(open(r"C:\Users\Windows\house price\save_models\house_Prediction_model.sav", "rb"))

scaler = pickle.load(open(r"C:\Users\Windows\house price\save_models\scaler.sav", "rb"))

st.set_page_config(page_title="Chennai House Price Predictor", layout="centered", page_icon="🏠")
st.title("🏠 Chennai House Price Prediction")
st.markdown("Enter all the property details to predict the house price in Chennai.")

# 🔢 Numeric Features
numeric_features = [
    "INT_SQFT", "DIST_MAINROAD", "N_BEDROOM", "N_BATHROOM",
    "N_ROOM", "QS_ROOMS", "QS_BATHROOM", "QS_BEDROOM",
    "QS_OVERALL", "REG_FEE", "COMMIS"
]

# 🧠 Categorical Mappings
sale_cond_map = {
    'Normal': 0, 'Abnormal': 1, 'Adj Land': 2,
    'Family': 3, 'Alloca': 4
}

buildtype_map = {
    '1Fam': 0, '2fmCon': 1, 'Duplex': 2,
    'TwnhsE': 3, 'TwnhsI': 4
}

utility_map = {
    'AllPub': 0, 'NoSewr': 1, 'NoSeWa': 2, 'OthWtr': 3
}

street_map = {
    'Paved': 0, 'Gravel': 1, 'None': 2
}

mzzone_map = {
    'A': 0, 'C': 1, 'I': 2
}

# 🚧 User Input Section
user_inputs = []

st.subheader("🧮 Numeric Property Details")
for feature in numeric_features:
    value = st.number_input(f"{feature}", min_value=0.0, step=1.0, format="%.2f")
    user_inputs.append(value)

st.subheader("🏡 Categorical Property Info")
sale_cond = st.selectbox("Sale Condition", list(sale_cond_map.keys()))
park_facil = st.radio("Parking Facility", ['Yes', 'No'])
buildtype = st.selectbox("Building Type", list(buildtype_map.keys()))
utility_avail = st.selectbox("Utility Availability", list(utility_map.keys()))
street = st.selectbox("Street Type", list(street_map.keys()))
mzzone = st.selectbox("Zone", list(mzzone_map.keys()))

# Append encoded categorical features
user_inputs.append(sale_cond_map[sale_cond])
user_inputs.append(1 if park_facil == 'Yes' else 0)
user_inputs.append(buildtype_map[buildtype])
user_inputs.append(utility_map[utility_avail])
user_inputs.append(street_map[street])
user_inputs.append(mzzone_map[mzzone])

# 🕒 Date Inputs
st.subheader("📅 Date Information")
date_build = st.date_input("Year of Building Construction")
date_sale = st.date_input("Date of Sale")

# Convert to timestamp
user_inputs.append(pd.to_datetime(date_build).timestamp())
user_inputs.append(pd.to_datetime(date_sale).timestamp())

# 🌐 Misc Info (non-model inputs)
st.subheader("🔤 Additional Info")
area = st.text_input("Area")
prt_id = st.text_input("Property ID")

# These two values are kept for display/log but not used for prediction.
# You can append dummy values or drop them depending on model training.
user_inputs.append(0)  # Placeholder for AREA
user_inputs.append(0)  # Placeholder for PRT_ID

# 🎯 Predict button
if st.button("Predict Price"):
    try:
        input_array = np.array(user_inputs).reshape(1, -1)
        scaled_input = scaler.transform(input_array)
        predicted_price = model.predict(scaled_input)[0]

        usd_to_inr = 82
        predicted_inr = predicted_price * usd_to_inr

        st.success(f"🏡 Estimated House Price: ₹{predicted_inr:,.2f} INR")

    except Exception as e:
        st.error(f"Error during prediction: {str(e)}")
