import pandas as pd

# Load dataset
df = pd.read_csv("car data.csv")

# Remove duplicate rows
df = df.drop_duplicates().copy()

# ==============================
# Feature Engineering
# ==============================

# Calculate car age
current_year = 2026
df["Car_Age"] = current_year - df["Year"]

# Remove Year because Car_Age contains more useful information
df = df.drop("Year", axis=1)

# Remove Car_Name
df = df.drop("Car_Name", axis=1)

# ==============================
# Encode Categorical Features
# ==============================

df = pd.get_dummies(
    df,
    columns=["Fuel_Type", "Selling_type", "Transmission"],
    drop_first=True
)

# ==============================
# Display Processed Data
# ==============================

print("========== PROCESSED DATA ==========")
print(df.head())

print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

# Save processed dataset
df.to_csv("processed_car_data.csv", index=False)

print("\nProcessed dataset saved as: processed_car_data.csv")