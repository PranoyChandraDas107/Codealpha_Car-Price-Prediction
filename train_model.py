import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score


# Load processed dataset
df = pd.read_csv("processed_car_data.csv")

# Separate features and target
X = df.drop("Selling_Price", axis=1)
y = df["Selling_Price"]


# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)


# Create Decision Tree model
model = DecisionTreeRegressor(
    random_state=42
)

# Train model
model.fit(X_train, y_train)


# Make predictions
y_pred = model.predict(X_test)


# Evaluation
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)


print("========== DECISION TREE PERFORMANCE ==========")
print(f"MAE  : {mae:.4f}")
print(f"MSE  : {mse:.4f}")
print(f"RMSE : {rmse:.4f}")
print(f"R2   : {r2:.4f}")


# Save model
joblib.dump(model, "car_price_model.pkl")

print("\nModel saved as: car_price_model.pkl")


# ==============================
# Actual vs Predicted Plot
# ==============================

plt.figure(figsize=(8, 6))

plt.scatter(y_test, y_pred)

plt.xlabel("Actual Selling Price")
plt.ylabel("Predicted Selling Price")
plt.title("Actual vs Predicted Car Prices")

# Perfect prediction reference line
min_price = min(y_test.min(), y_pred.min())
max_price = max(y_test.max(), y_pred.max())

plt.plot(
    [min_price, max_price],
    [min_price, max_price],
    linestyle="--"
)

plt.tight_layout()
plt.show()


# ==============================
# Feature Importance
# ==============================

feature_importance = pd.Series(
    model.feature_importances_,
    index=X.columns
).sort_values(ascending=False)

print("\n========== FEATURE IMPORTANCE ==========")
print(feature_importance)


plt.figure(figsize=(9, 6))

feature_importance.sort_values().plot(kind="barh")

plt.title("Feature Importance")
plt.xlabel("Importance")
plt.ylabel("Feature")

plt.tight_layout()
plt.show()