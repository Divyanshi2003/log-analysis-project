import pandas as pd

# Step 1: Read the CSV file
try:
    df = pd.read_csv("Commerce_logs.csv")
    print("📄 Successfully loaded Commerce_logs.csv")
except Exception as e:
    print(f"❌ Error loading CSV: {e}")
    exit()

# Step 2: Calculate churn risk
# Churn if: sales == 0 OR (returned == "Yes" and returned_amount > 0)
df["churn_risk"] = ((df["sales"] == 0) | ((df["returned"] == "Yes") & (df["returned_amount"] > 0))).astype(int)

# Step 3: Select relevant columns
result = df[[
    "age",
    "gender",
    "country",
    "sales",
    "returned",
    "returned_amount",
    "churn_risk"
]]

# Step 4: Save to a new CSV
try:
    result.to_csv("churn_results.csv", index=False)
    print("✅ churn_results.csv created successfully!")
except Exception as e:
    print(f"❌ Error saving CSV: {e}")
