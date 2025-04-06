# Chennai House Price Prediction 🏠💰

This project uses machine learning regression models to predict house prices in Chennai, achieving 95% accuracy. The project includes a **Streamlit UI** for real-time price predictions and a **frontend website** built with HTML, CSS, and JavaScript for an interactive user experience.

## 📌 Overview

The primary goal of this project is to predict house prices in Chennai using various machine learning models. The models used in this project include:

- **Linear Regression**
- **Decision Tree**
- **Random Forest**
- **Support Vector Regression (SVR)**
- **XGBoost**
- **K-Nearest Neighbors (KNN)**
- **Extra Trees Regressor**

The Streamlit UI allows users to input property details and receive instant price predictions, while the frontend website provides an easy-to-use interface for exploring the project.

## 🚀 Features

### 🧮 Numeric Property Details
- `INT_SQFT`: Total square footage of the property
- `DIST_MAINROAD`: Distance from the main road (in meters)
- `N_BEDROOM`: Number of bedrooms
- `N_BATHROOM`: Number of bathrooms
- `N_ROOM`: Total number of rooms
- `QS_ROOMS`: Quality score for rooms
- `QS_BATHROOM`: Quality score for bathrooms
- `QS_BEDROOM`: Quality score for bedrooms
- `QS_OVERALL`: Overall quality score of the property
- `REG_FEE`: Registration fee (in INR)
- `COMMIS`: Commission for the sale

### 🏡 Categorical Property Information
- `Sale Condition`: Normal or Abnormal
- `Parking Facility`: Available or Not Available
- `Building Type`: 1Fam, 2Fam, etc.
- `Utility Availability`: AllPub or Partial
- `Street Type`: Paved or Unpaved
- `Zone`: Residential or Commercial

### 📅 Date Information
- `Year of Building Construction`: Year the property was built
- `Area`: Geographical zone where the property is located
- `Property ID`: Unique ID for each property

## 🖥️ Usage

### Streamlit UI
1. Input 20 property features (both numeric and categorical).
2. Click **Predict** to get the estimated price of the property.
3. View the results in INR with a confidence score.

### Frontend Website
1. Explore project details, features, and model performance.
2. Navigate to the **Prediction** page to interact with the model and get predictions.

## 📂 Project Structure



├── data/                   # Dataset (CSV files)
├── models/                 # Trained models (e.g., modelmlg.pkl)
├── frontend/               # HTML/CSS/JS files
│   ├── index.html
│   ├── styles.css
│   └── script.js
├── app.py                  # Streamlit application
├── requirements.txt        # Dependencies
└── README.md


## 🤖 Models Used

- **Linear Regression**
- **DecisionTreeRegressor**
- **RandomForestRegressor**
- **SVR**
- **xgb.XGBRegressor**
- **KNeighborsRegressor** (n_neighbors=5)
- **ExtraTreesRegressor**

## 📊 Performance

- **Accuracy**: 95% (R² score)
- **Best Model**: Random Forest Regressor (based on cross-validation)

---

This project leverages multiple machine learning models to deliver highly accurate house price predictions, providing an easy-to-use interface for users to interact with the model and gain insights about property prices in Chennai.
