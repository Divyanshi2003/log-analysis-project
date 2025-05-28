import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the churn data
df = pd.read_csv("churn_results.csv")

# Set Seaborn theme
sns.set(style="whitegrid")

# --- 1. Churn vs Non-Churn by Gender ---
plt.figure(figsize=(6, 4))
sns.countplot(data=df, x='gender', hue='churn_risk', palette='Set2')
plt.title("Churn vs Non-Churn by Gender")
plt.xlabel("Gender")
plt.ylabel("Number of Users")
plt.legend(title='Churn Risk', labels=['No Churn (0)', 'Churn (1)'])
plt.tight_layout()
plt.savefig("churn_by_gender.png")
plt.show()

# --- 2. Churn vs Non-Churn by Country ---
plt.figure(figsize=(10, 5))
sns.countplot(data=df, x='country', hue='churn_risk', palette='Set3')
plt.title("Churn vs Non-Churn by Country")
plt.xlabel("Country")
plt.ylabel("Number of Users")
plt.legend(title='Churn Risk', labels=['No Churn (0)', 'Churn (1)'])
plt.tight_layout()
plt.savefig("churn_by_country.png")
plt.show()

# --- 3. Churn vs Non-Churn by Age (binned) ---
df['age_group'] = pd.cut(df['age'], bins=[10, 20, 30, 40, 50, 60, 100], labels=['10s', '20s', '30s', '40s', '50s', '60+'])

plt.figure(figsize=(8, 4))
sns.countplot(data=df, x='age_group', hue='churn_risk', palette='coolwarm')
plt.title("Churn vs Non-Churn by Age Group")
plt.xlabel("Age Group")
plt.ylabel("Number of Users")
plt.legend(title='Churn Risk', labels=['No Churn (0)', 'Churn (1)'])
plt.tight_layout()
plt.savefig("churn_by_age.png")
plt.show()
