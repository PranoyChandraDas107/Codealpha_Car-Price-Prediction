import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("car data.csv")

# Remove duplicate rows
df = df.drop_duplicates()

print("Dataset shape after removing duplicates:", df.shape)

# ==============================
# 1. Selling Price Distribution
# ==============================

plt.figure(figsize=(8, 5))
sns.histplot(df["Selling_Price"], kde=True)
plt.title("Distribution of Selling Price")
plt.xlabel("Selling Price")
plt.ylabel("Frequency")
plt.tight_layout()
plt.show()


# ==============================
# 2. Present Price vs Selling Price
# ==============================

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Present_Price",
    y="Selling_Price"
)
plt.title("Present Price vs Selling Price")
plt.xlabel("Present Price")
plt.ylabel("Selling Price")
plt.tight_layout()
plt.show()


# ==============================
# 3. Year vs Selling Price
# ==============================

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Year",
    y="Selling_Price"
)
plt.title("Year vs Selling Price")
plt.xlabel("Manufacturing Year")
plt.ylabel("Selling Price")
plt.tight_layout()
plt.show()


# ==============================
# 4. Driven KMs vs Selling Price
# ==============================

plt.figure(figsize=(8, 5))
sns.scatterplot(
    data=df,
    x="Driven_kms",
    y="Selling_Price"
)
plt.title("Driven KMs vs Selling Price")
plt.xlabel("Driven Kilometers")
plt.ylabel("Selling Price")
plt.tight_layout()
plt.show()


# ==============================
# 5. Fuel Type vs Selling Price
# ==============================

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="Fuel_Type",
    y="Selling_Price"
)
plt.title("Fuel Type vs Selling Price")
plt.xlabel("Fuel Type")
plt.ylabel("Selling Price")
plt.tight_layout()
plt.show()


# ==============================
# 6. Transmission vs Selling Price
# ==============================

plt.figure(figsize=(8, 5))
sns.boxplot(
    data=df,
    x="Transmission",
    y="Selling_Price"
)
plt.title("Transmission vs Selling Price")
plt.xlabel("Transmission")
plt.ylabel("Selling Price")
plt.tight_layout()
plt.show()


# ==============================
# 7. Correlation Heatmap
# ==============================

numeric_df = df.select_dtypes(include=["int64", "float64"])

plt.figure(figsize=(9, 6))
sns.heatmap(
    numeric_df.corr(),
    annot=True,
    cmap="coolwarm",
    fmt=".2f"
)
plt.title("Correlation Heatmap")
plt.tight_layout()
plt.show()