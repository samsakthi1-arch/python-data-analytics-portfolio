import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# Load our dataset for today — a housing price dataset
url = "https://raw.githubusercontent.com/ageron/handson-ml/master/datasets/housing/housing.csv"
df = pd.read_csv(url)

print("Dataset loaded.")
print(f"Shape: {df.shape}")

# What are the columns?
print("\nColumns:")
print(df.columns.tolist())

# What data type is each column?
print("\nData Types:")
print(df.dtypes)

missing = df.isnull().sum()
print("Missing values per column:")
print(missing)

# Express as a percentage of total rows
print("\nMissing as % of total:")
print((missing / len(df) * 100).round(2))

# Look at the first 5 rows
print(df.head())

# Look at a random sample — sometimes more revealing than the first rows
print(df.sample(5, random_state=10))

print(df.describe())

# Plot distributions for all numerical columns at once
numerical_cols = df.select_dtypes(include="number").columns


fig, axes = plt.subplots(3, 3, figsize=(14, 10))
axes = axes.flatten()   # Convert 3x3 grid to a flat list for easy looping


for i, col in enumerate(numerical_cols):
   sns.histplot(data=df, x=col, kde=True, ax=axes[i], color="steelblue")
   axes[i].set_title(col, fontsize=10)
   axes[i].set_xlabel("")


plt.suptitle("Distribution of All Numerical Features", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()

# Calculate skewness for every numerical column
skewness = df.select_dtypes(include="number").skew().sort_values(ascending=False)
print("Skewness by column:")
print(skewness.round(2))

# -0.5 to 0.5 -> normal range
# -1 and 1

import seaborn as sns
import matplotlib.pyplot as plt


# Step 1: Compute the correlation matrix
corr_matrix = df.select_dtypes(include="number").corr()


# Step 2: Build the heatmap
plt.figure(figsize=(10, 8))
sns.heatmap(
   corr_matrix,
   annot=True,
   fmt=".2f",
   cmap="coolwarm",
   vmin=-1,
   vmax=1,
   square=True,
   linewidths=0.5
)
plt.title("Correlation Matrix — Housing Dataset", fontsize=14, fontweight="bold")
plt.tight_layout()
plt.show()