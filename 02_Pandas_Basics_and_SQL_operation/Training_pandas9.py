import pandas as pd


scores = pd.Series([78, 92, 85, 60, 95])
print(scores)


scores = pd.Series([78, 92, 85, 60, 95],
                  index=["Ali", "Sara", "John", "Maya", "Tom"])
print(scores)

pd.Series([10, "twenty", 30])

data = {
   "Name":  ["Ali", "Sara", "John", "Maya"],
   "Score": [78, 92, 85, 60],
   "Grade": ["B", "A", "B", "C"]
}


df = pd.DataFrame(data)
print(df)
print(df.shape)    # (rows, columns)
print(df.columns)  # column names
print(df.dtypes)   # data types of each column

data_text = """Name,Score,Grade,Age
Ali,78,B,20
Sara,92,A,22
John,85,B,21
Maya,60,C,20
Tom,95,A,23
Rita,72,C,22"""

with open("students.csv", "w") as f:
   f.write(data_text)


print("File created!")

df = pd.read_csv("students.csv")
print(df)

print(df.head())    # First 5 rows
print(df.tail())    # Last 5 rows
print(df.head(2))   # First 2 rows — you choose how many

print(df.info())

print(df.describe())   # Statistics for number columns

print(df["Score"])

print(df["Score"].mean())   # Average
print(df["Score"].max())    # Highest score
print(df["Score"].min())    # Lowest score

print(df[["Name", "Score"]])

print(df["Score"])

df[["Score", "Age"]]

print(df[df["Score"] > 80])

print(df["Score"] > 80)

print(df[df["Grade"] == "A"])

print(df[(df["Score"] > 75) & (df["Age"] < 22)])

# Load data
df = pd.read_csv("students.csv")


# Quick overview
print("=== Student Report ===")
print(f"Total students: {len(df)}")
print(f"Average score:  {df['Score'].mean():.1f}")
print(f"Highest score:  {df['Score'].max()}")
print(f"Lowest score:   {df['Score'].min()}")

# Find top performers (score above average)
avg = df["Score"].mean()
top_students = df[df["Score"] > avg]


print(f"Class average: {avg:.1f}")
print(f"\nTop performers ({len(top_students)} students):")
print(top_students[["Name", "Score", "Grade"]])

# Find the best student
best = df[df["Score"] == df["Score"].max()]
print(f"\nBest student:")
print(best[["Name", "Score"]])

# Find the best student
best = df[df["Score"] == df["Score"].max()]
print(f"\nBest student:")
print(best[["Name", "Score"]])