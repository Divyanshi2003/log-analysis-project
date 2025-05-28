import pandas as pd

# File paths
input_file = "Commerce_logs.csv"
output_file = "daily_avg_duration.csv"

try:
    # Load CSV
    df = pd.read_csv(input_file)

    # Convert accessed_date to datetime
    df['accessed_date'] = pd.to_datetime(df['accessed_date'])

    # Extract just the date part (drop time)
    df['date'] = df['accessed_date'].dt.date

    # Group by date and calculate average duration
    daily_avg = df.groupby('date')['duration_(secs)'].mean().reset_index()

    # Rename for clarity
    daily_avg.columns = ['date', 'average_duration_secs']

    # Save to CSV
    daily_avg.to_csv(output_file, index=False)

    print(f"✅ Daily average duration saved to: {output_file}")
    print(daily_avg.head())

except Exception as e:
    print(f"⚠️ Error: {e}")
