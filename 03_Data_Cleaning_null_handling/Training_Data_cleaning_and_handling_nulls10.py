import pandas as pd


data = {
   "Name":  ["Ali", "Sara", "John", "Maya", "John", None, "Tom"],
   "Score": [78, None, 85, 60, 85, 92, None],
   "Grade": ["B", "A", "B", "C", "B", "A", "A"],
   "Age":   [20, 22, None, 20, None, 23, 21]
}


df = pd.DataFrame(data)
print(df)

print(df.isnull())

print((df.isnull().sum() / len(df) * 100).round(1))

print(df[df.isnull().any(axis=1)])

# Drop any row with at least one null
df_dropped = df.dropna()
print(df_dropped)
print(len(df_dropped))

# Only drop rows where Score is missing
df_score_clean = df.dropna(subset=["Score"])
print(df_score_clean)

# Drop an entire column
df_no_age = df.drop(columns=["Age"])
print(df_no_age)

# Fill missing Name with "Unknown"
df_filled = df.copy()   # always work on a copy
df_filled["Name"] = df_filled["Name"].fillna("Unknown")
print(df_filled[["Name", "Score"]])

# Fill Score with the mean
score_mean = df_filled["Score"].mean()
print(score_mean)
df_filled["Score"] = df_filled["Score"].fillna(score_mean)
print(df_filled[["Name", "Score"]])

# Fill Age with median
age_median = df_filled["Age"].median()
df_filled["Age"] = df_filled["Age"].fillna(age_median)
print(df_filled)

print(df_filled.isnull().sum())

print(df)

print(df.duplicated())

print(df.duplicated().sum())

print(df[df.duplicated()])

df_no_dupes = df.drop_duplicates()
print(len(df))
print(len(df_no_dupes))
print(df_no_dupes)

df.drop_duplicates(keep="last")

df.drop_duplicates(keep=False)

print(df[df.duplicated(subset=["Grade"], keep=False)])

print(df_filled.dtypes)

df_filled["Grade"] = df_filled["Grade"].astype("category")
print(df_filled["Grade"].dtype)
print(df_filled["Grade"].cat.categories)

print(df_filled["Grade"].value_counts())

# Simulate a broken column loaded as text
df_filled["Score_text"] = df_filled["Score"].astype(str)
print(df_filled["Score_text"].dtype)

df_filled["Score_fixed"] = pd.to_numeric(df_filled["Score_text"], errors="coerce")
print(df_filled["Score_fixed"].dtype)
print(df_filled["Score_fixed"].mean())

import pandas as pd


def null_report(df):
   total_rows = len(df)
   null_counts = df.isnull().sum()
   null_pct = (null_counts / total_rows * 100).round(1)


   print("=== NULL REPORT ===")
   print(f"Total rows: {total_rows}")
   print(f"Total columns: {len(df.columns)}\n")


   for col in df.columns:
       count = null_counts[col]
       pct = null_pct[col]
       status = "✓ CLEAN" if count == 0 else f"✗ {count} missing ({pct}%)"
       print(f"  {col:<10} {status}")


# --- Run it ---
data = {
   "Name":  ["Ali", "Sara", "John", None, "Tom"],
   "Score": [78, None, 85, 92, None],
   "Grade": ["B", "A", "B", "A", "A"]
}
df = pd.DataFrame(data)
null_report(df)
