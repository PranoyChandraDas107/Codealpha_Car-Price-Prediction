import pandas as pd

# Load dataset
df = pd.read_csv("car data.csv")

print("========== FIRST 5 ROWS ==========")
print(df.head())

print("\n========== DATASET SHAPE ==========")
print(df.shape)

print("\n========== COLUMN NAMES ==========")
print(df.columns.tolist())

print("\n========== DATA TYPES ==========")
print(df.dtypes)

print("\n========== MISSING VALUES ==========")
print(df.isnull().sum())

print("\n========== DUPLICATE ROWS ==========")
print(df.duplicated().sum())

print("\n========== STATISTICAL SUMMARY ==========")
print(df.describe())

print("\n========== UNIQUE VALUES ==========")
for column in df.columns:
    print(f"{column}: {df[column].nunique()}")