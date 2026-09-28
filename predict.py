import pandas as pd
import joblib


# Load trained model
model = joblib.load("car_price_model.pkl")


print("========== CAR PRICE PREDICTION ==========")

# User input
present_price = float(input("Enter Present Price: "))
driven_kms = int(input("Enter Driven KMs: "))
owner = int(input("Enter Number of Previous Owners: "))
car_age = int(input("Enter Car Age: "))

print("\nFuel Type:")
print("1. Diesel")
print("2. Petrol")

fuel_choice = input("Enter choice: ")

fuel_diesel = 1 if fuel_choice == "1" else 0
fuel_petrol = 1 if fuel_choice == "2" else 0


print("\nSelling Type:")
print("1. Dealer")
print("2. Individual")

selling_choice = input("Enter choice: ")

selling_individual = 1 if selling_choice == "2" else 0


print("\nTransmission:")
print("1. Manual")
print("2. Automatic")

transmission_choice = input("Enter choice: ")

transmission_manual = 1 if transmission_choice == "1" else 0


# Create input dataframe
input_data = pd.DataFrame([{
    "Present_Price": present_price,
    "Driven_kms": driven_kms,
    "Owner": owner,
    "Car_Age": car_age,
    "Fuel_Type_Diesel": fuel_diesel,
    "Fuel_Type_Petrol": fuel_petrol,
    "Selling_type_Individual": selling_individual,
    "Transmission_Manual": transmission_manual
}])


# Prediction
prediction = model.predict(input_data)[0]


print("\n==")
print(f"Predicted Selling Price: {prediction:.2f}")
print("==")