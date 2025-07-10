from sklearn.pipeline import Pipeline
import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load model
try:
    with open("random_forest_regressor_model.pkl", "rb") as f:
        model = pickle.load(f)
except FileNotFoundError:
    st.error("🚫 Model file not found. Please ensure the model is present.")
    st.stop()

# Page config
st.set_page_config(page_title="Rent Predictor", layout="wide")

# Custom CSS
st.markdown("""
    <style>
    html, body, [class*="css"]  {
        font-family: 'Segoe UI', sans-serif;
        background-color: #f4f6f9;
        color: #333;
    }

    .main-title {
        font-size: 42px;
        font-weight: 700;
        text-align: center;
        margin-top: 20px;
        color: #333333;
    }

    .subtitle {
        font-size: 18px;
        text-align: center;
        color: #555555;
        margin-bottom: 40px;
    }

    .stButton>button {
        background-color: #009688;
        color: white;
        padding: 0.75em 2em;
        border-radius: 8px;
        font-size: 18px;
        border: none;
        margin-top: 30px;
        width: 100%;
        transition: background-color 0.3s ease;
    }

    .stButton>button:hover {
        background-color: #00796b;
    }

    .rent-box {
        background-color: #e0f2f1;
        padding: 30px;
        border-radius: 10px;
        text-align: center;
        margin-top: 30px;
        color: #004d40;
        font-size: 26px;
        font-weight: bold;
    }

    footer {
        text-align: center;
        font-size: 14px;
        color: #999999;
        padding-top: 40px;
        margin-top: 60px;
    }

    @media only screen and (max-width: 768px) {
        .stButton>button {
            font-size: 16px;
        }
    }
    </style>
""", unsafe_allow_html=True)

# Header
st.markdown("<div class='main-title'>🏡 Apartment  Rent Predictor</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Fill in property details to estimate the monthly rent</div>", unsafe_allow_html=True)

# Input layout
with st.container():
    col1, col2 = st.columns(2)

    with col1:
        bhk = st.slider('BHK (Bedrooms)', 1, 6, 3)
        bath = st.slider('Bathrooms', 1, 7, 2)
        rent_floor = st.slider('Rental Floor', -2, 22, 0)
        total_floors = st.slider('Total Floors in Building', 1, 30, 10)
        fixed_size = st.slider("Total Area (Sqft)", 100, 3100, 850, step=50)

    with col2:
        sqft_rent = st.slider("Per Sqft Rent (₹)", 10, 120, 35, step=5)
        city = st.selectbox('City', ['Kolkata', 'Mumbai', 'Bangalore', 'Delhi', 'Chennai', 'Hyderabad'])
        furnish = st.selectbox('Furnishing Status', ['Unfurnished', 'Semi-Furnished', 'Furnished'])
        tenant = st.selectbox('Tenant Preference', ['Bachelors/Family', 'Bachelors', 'Family'])
        contact = st.selectbox('Point of Contact', ['Contact Owner', 'Contact Agent'])

# Validation
if rent_floor > total_floors:
    st.warning("⚠️ Rental floor cannot be greater than total floors.")
    st.stop()

# Prepare input
input_data = pd.DataFrame([[
    bhk, city, furnish, tenant, bath, contact,
    rent_floor, total_floors, fixed_size, sqft_rent
]], columns=[
    'BHK', 'City', 'Furnishing Status', 'Tenant Preferred', 'Bathroom',
    'Point of Contact', 'Rental Floor', 'Total Number of Floor', 'Fixed Size', 'Square Feet Rent'
])

# Predict
if st.button("🔍 Predict Rent"):
    prediction = model.predict(input_data)
    rent = np.round(prediction[0], 2)
    st.markdown(f"<div class='rent-box'>💰 Estimated Monthly Rent: ₹ {rent}</div>", unsafe_allow_html=True)

# Footer
st.markdown("<footer>Made with ❤️ by Pradeep Rawat</footer>", unsafe_allow_html=True)
