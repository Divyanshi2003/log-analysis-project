
import os
import pandas as pd

# File path
input_file = "Commerce_logs.csv"


# Define the directory path
directory_path = "csv"

# Check if the directory exists
if not os.path.exists(directory_path):
    os.makedirs(directory_path)
    print(f"Directory '{directory_path}' created.")
else:
    print(f"Directory '{directory_path}' already exists.")


try:
    # Load data
    df = pd.read_csv(input_file)

    # Ensure duration is numeric
    df['duration_(secs)'] = pd.to_numeric(df['duration_(secs)'], errors='coerce')

    # Drop rows with missing or invalid durations
    df = df.dropna(subset=['duration_(secs)'])

    # Overall average duration
    overall_avg = df['duration_(secs)'].mean()

    print("🕒 Average Session Duration Analysis")
    print(f"• Overall Average Duration: {overall_avg:.2f} seconds\n")

    # Average by Age
    avg_by_age = df.groupby('age')['duration_(secs)'].mean().reset_index().sort_values(by='duration_(secs)', ascending=False)
    print("📊 Average Duration by Age:")
    print(avg_by_age.head())

    # Average by Gender
    avg_by_gender = df.groupby('gender')['duration_(secs)'].mean().reset_index().sort_values(by='duration_(secs)', ascending=False)
    print("\n📊 Average Duration by Gender:")
    print(avg_by_gender)

    # Average by Country
    avg_by_country = df.groupby('country')['duration_(secs)'].mean().reset_index().sort_values(by='duration_(secs)', ascending=False)
    print("\n🌍 Average Duration by Country:")
    print(avg_by_country.head(10))  # top 10 countries

    # Save all to CSVs if needed
    avg_by_age.to_csv("csv/avg_duration_by_age.csv", index=False)
    avg_by_gender.to_csv("csv/avg_duration_by_gender.csv", index=False)
    avg_by_country.to_csv("csv/avg_duration_by_country.csv", index=False)

except Exception as e:
    print(f"⚠️ Error: {e}")
