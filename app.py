
import streamlit as st
import numpy as np
import pandas as pd
import pickle

# Load model
with open("random_forest_regressor_model.pkl", "rb") as f:
    model = pickle.load(f)

# Page config
st.set_page_config(page_title="House Rent Predictor", layout="wide")

# Inject custom CSS
st.markdown("""
    <style>
    body {
        background-color: #121212;
        color: white;
        font-family: 'Arial', sans-serif;
    }

       .title {
        color: white;
        font-size: 36px;
        text-align: center;
        font-weight: bold;
        margin-bottom: 10px;
    }

    .subtitle {
        color: #cccccc;
        font-size: 18px;
        text-align: center;
        margin-bottom: 40px;
    }

    .stSlider label, .stSelectbox label, .stButton button {
        font-size: 18px !important;
        color: white !important;
    }

    .stSelectbox div[role="combobox"] {
        font-size: 18px;
    }

    .stSlider .st-b6 {
        font-size: 16px !important;
    }

    .stButton button {
        background-color: #00cc99;
        color: black;
        padding: 10px 24px;
        border-radius: 8px;
        font-size: 18px;
        align-items: center;
        justify-content: center;
        margin-left: 50%;
        transform: translateX(-50%);
    }
    </style>
""", unsafe_allow_html=True)

# Main black container

with st.container():
   

    st.markdown('<div class="title">🏠 House Rent Predictor</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Enter house details below to get the estimated monthly rent</div>', unsafe_allow_html=True)

    # Input Section
    col1, col2 = st.columns(2)

    with col1:
        bhk = st.slider('BHK (Bedrooms)', 1, 6, 3)
        bath = st.slider('Bathrooms', 1, 7, 2)
        rent = st.slider('Rental Floor', -2, 22, 0)
        total_f = st.slider('Total Floors in Building', 0, 30, 10)
        fixed_s = st.slider("Total Area (Sqft)", 10, 3100, 850, step=10)

    with col2:
        square_feet_rent = st.slider("Per Sqft Rent (₹)", 10, 120, 35, step=2)
        city = st.selectbox('City', ['Kolkata', 'Mumbai', 'Bangalore', 'Delhi', 'Chennai', 'Hyderabad'])
        furn_s = st.selectbox('Furnishing Status', ['Unfurnished', 'Semi-Furnished', 'Furnished'])
        tenant = st.selectbox('Tenant Preference', ['Bachelors/Family', 'Bachelors', 'Family'])
        point_c = st.selectbox('Point of Contact', ['Contact Owner', 'Contact Agent'])

    new_data = pd.DataFrame([[bhk, city, furn_s, tenant, bath, point_c, rent, total_f, fixed_s, square_feet_rent]],
        columns=[
            'BHK', 'City', 'Furnishing Status', 'Tenant Preferred',
            'Bathroom', 'Point of Contact', 'Rental Floor',
            'Total Number of Floor', 'Fixed Size', "Square Feet Rent"
        ]
    )

    if st.button('Predict Rent'):
        prediction = model.predict(new_data)
        predicted_rent = np.round(prediction[0], 2)
        st.markdown(f"""
          <div style='
        background-color: #00cc99;
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        color: black;
        font-size: 24px;
        font-weight: bold;
        margin-top: 30px;
    '>
        💰 Estimated Monthly Rent: ₹ {predicted_rent}
    </div> """, unsafe_allow_html=True)
        


