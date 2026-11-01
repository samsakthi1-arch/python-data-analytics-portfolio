import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import plotly.express as px


print("All libraries loaded successfully")

import matplotlib.pyplot as plt

months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales  = [120, 145, 98, 167, 210]


plt.plot(months, sales)
plt.show()


import matplotlib.pyplot as plt


months = ["Jan", "Feb", "Mar", "Apr", "May"]
sales  = [120, 145, 98, 167, 210]

plt.figure(figsize=(8, 5))          # Set canvas size (width, height in inches)
plt.plot(months, sales,
        color="steelblue",
        linewidth=2,
        marker="o")  

plt.title("Monthly Sales Performance", fontsize=14, fontweight="bold")
plt.xlabel("Month")
plt.ylabel("Units Sold")
plt.grid(True, linestyle="--", alpha=0.5)   # alpha controls transparency
plt.tight_layout()                           # prevents labels from being cut off
plt.show()


plt.bar(months, sales, color="steelblue")   # bar instead of plot

import matplotlib.pyplot as plt
import numpy as np


x = np.linspace(0, 10, 100) 

fig, axes = plt.subplots(1, 2, figsize=(12, 5))  # 1 row, 2 columns
# Left chart
axes[0].plot(x, np.sin(x), color="steelblue")
axes[0].set_title("Sine Wave")
axes[0].set_xlabel("x")
axes[0].set_ylabel("sin(x)")

# Right chart
axes[1].plot(x, np.cos(x), color="coral")
axes[1].set_title("Cosine Wave")
axes[1].set_xlabel("x")
axes[1].set_ylabel("cos(x)")

plt.tight_layout()
plt.show()

plt.savefig("sales_chart.png", dpi=150, bbox_inches="tight")

import seaborn as sns
import pandas as pd

df = sns.load_dataset("tips")
print(df.head())
print(df.shape)


sns.histplot(data=df, x="total_bill", bins=20, kde=True, color="steelblue")
# kde=True adds a smooth curve showing the overall shape of the distribution

plt.title("Distribution of Total Bill Amounts")
plt.xlabel("Total Bill ($)")
plt.ylabel("Count")
plt.tight_layout()
plt.show()

sns.scatterplot(data=df,
               x="total_bill",
               y="tip",
               hue="time",        # Color points by meal time (Lunch/Dinner)
               style="smoker",    # Different marker shape for smokers vs non-smokers
               alpha=0.7)


plt.title("Tip vs. Total Bill by Meal Time")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.tight_layout()
plt.show()

sns.boxplot(data=df,
           x="day",
           y="total_bill",
           hue="sex",
           palette="Set2")

plt.title("Bill Distribution by Day and Gender")
plt.xlabel("Day of Week")
plt.ylabel("Total Bill ($)")
plt.tight_layout()
plt.show()

df = sns.load_dataset("tips")


# Step 1: Compute correlation — only works on numeric columns
corr_matrix = df.select_dtypes(include="number").corr()


# Step 2: Plot the heatmap
sns.heatmap(corr_matrix,
           annot=True,       # Show the actual numbers inside each cell
           fmt=".2f",        # Format numbers to 2 decimal places
           cmap="coolwarm",  # Color scale: blue = negative, red = positive
           vmin=-1, vmax=1)  # Fix the scale from -1 to 1


plt.title("Correlation Matrix — Tips Dataset")
plt.tight_layout()
plt.show()

import plotly.express as px
import pandas as pd


df = px.data.tips()   # Plotly has its own built-in datasets


fig = px.scatter(df, x="total_bill", y="tip")
fig.show()

import plotly.express as px


df = px.data.tips()


fig = px.scatter(
   df,
   x="total_bill",
   y="tip",
   color="time",           # Color by Lunch/Dinner
   size="size",            # Bubble size = party size
   hover_data=["day", "sex"],  # Extra fields shown on hover
   title="Restaurant Tips — Interactive Explorer",
   labels={"total_bill": "Total Bill ($)", "tip": "Tip ($)"}
)


fig.update_layout(
   width=800,
   height=500,
   template="plotly_white"   # Clean white background
)


fig.show()

# Bar chart
monthly = pd.DataFrame({
   "Month": ["Jan", "Feb", "Mar", "Apr", "May"],
   "Sales": [120, 145, 98, 167, 210]
})


fig = px.bar(monthly, x="Month", y="Sales",
            title="Monthly Sales",
            color="Sales",               # Color bars by value
            color_continuous_scale="Blues")
fig.show()
