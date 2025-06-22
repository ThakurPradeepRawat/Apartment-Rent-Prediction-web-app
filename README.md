
# 🏡 House Rent Prediction Web App

A web-based **House Rent Predictor** built using **Streamlit**, which estimates the monthly rent of a property based on input features such as BHK, city, furnishing status, and more. The model is powered by a **Random Forest Regressor**, trained on a cleaned dataset of house rentals.

---

## 🚀 Demo

> 💡 *This app runs locally via Streamlit. Deployment instructions are included below.*

---

## 📁 Project Structure

```
📦 House-Rent-Predictor/
├── app.py                       # Streamlit application
├── House_Rent.ipynb            # Jupyter notebook used for training and EDA
├── House_Rent_Dataset.csv      # Source dataset
├── random_forest_regressor_model.pkl  # Trained machine learning model
├── requirement.txt             # Python dependencies
└── README.md                   # Project documentation
```

---

## 📊 Features

- Input fields for:
  - BHK
  - Bathrooms
  - City
  - Furnishing status
  - Tenant preference
  - Rental floor, total floors
  - Square footage and per sq ft rent
  - Point of contact
- Clean, responsive UI with CSS styling
- Real-time rent predictions using a trained model

---

## 🧠 Machine Learning Model

- Model type: `RandomForestRegressor` (from `scikit-learn`)
- Features used: numeric + categorical (city, furnishing status, etc.)
- Trained in `House_Rent.ipynb` and saved as `random_forest_regressor_model.pkl`

---

## 🔧 Setup Instructions

1. **Clone the repo:**

```bash
git clone https://github.com/thakur pradeep rawat/house-rent-predictor.git
cd house-rent-predictor
```

2. **Create and activate a virtual environment (recommended):**

```bash
python -m venv venv
venv\Scripts\activate

```

3. **Install dependencies:**

```bash
pip install -r requirement.txt
```

4. **Run the Streamlit app:**

```bash
streamlit run app.py
```

---

## 📷 Preview

> *(Insert screenshot of the app UI here if you'd like)*

---

## 📌 Dependencies

See `requirement.txt`:

```
pandas
numpy
scikit-learn
streamlit
```

---

## 📬 Contact

Created by Pradeep Rawat – feel free to reach out via GitHub or email for suggestions or collaboration!
