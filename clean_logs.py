# clean_logs.py
import pandas as pd

# Load the CSV
df = pd.read_csv("Commerce_logs.csv")

# Create 'gender_short' column
gender_map = {"Female": "F", "Male": "M"}
df["gender_short"] = df["gender"].map(gender_map)

# Drop the original 'gender' column
df.drop(columns=["gender"], inplace=True)

# Display the cleaned data
print("🧹 Cleaned Data:")
print(df.head())

# Optional: Save to a new CSV
df.to_csv("cleaned_logs.csv", index=False)