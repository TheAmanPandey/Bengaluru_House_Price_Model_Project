# Bengaluru House Price Model

This project predicts **house prices in Bengaluru** based on various features such as:
- Total area (in square feet)
- Number of bathrooms
- Location
- BHK (Bedrooms, Hall, Kitchen)
The model is trained using **Machine Learning** techniques and deployed using **joblib** for persistence.

## Technologies Used
- **Python**
- **Pandas**, **NumPy**, **Scikit-learn**
- **Joblib** (for model saving & loading)
- **Jupyter Notebook** (for experiments and analysis)

## Workflow
1. **Data Cleaning & Preprocessing**
   - Handle missing values
   - Remove outliers (based on sqft & price per sqft)
   - One-Hot Encoding for location
2. **Model Training**
   - Linear Regression
3. **Model Saving**
   - Trained model saved using `joblib`
4. **Deployment**
   - Model can be loaded directly in Python for predictions

This project is open source. Feel free to fork, modify, and use it for learning purposes.
