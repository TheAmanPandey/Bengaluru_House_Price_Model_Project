import joblib

# Load the trained model
model = joblib.load("model/bengaluru_house_price_model.pkl")

# Example input: [sqft, bath, bhk]
example_input = [[1800, 2, 3]]

# Predict
predicted_price = model.predict(example_input)
print("Predicted Price:", predicted_price[0])