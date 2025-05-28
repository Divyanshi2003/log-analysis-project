import pandas as pd

# File paths
input_file = "Commerce_logs.csv"
output_file = "combined_peak_usage.csv"

try:
    # Load data
    df = pd.read_csv(input_file)

    # Parse datetime
    df['accessed_date'] = pd.to_datetime(df['accessed_date'])

    # Extract day name and hour
    df['day_of_week'] = df['accessed_date'].dt.day_name()
    df['hour'] = df['accessed_date'].dt.hour

    # Group by both day and hour
    combined_usage = df.groupby(['day_of_week', 'hour']).size().reset_index(name='access_count')

    # Order the days correctly
    day_order = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
    combined_usage['day_of_week'] = pd.Categorical(combined_usage['day_of_week'], categories=day_order, ordered=True)
    combined_usage = combined_usage.sort_values(['day_of_week', 'hour'])

    # Save to CSV
    combined_usage.to_csv(output_file, index=False)

    print("✅ Combined day/hour usage saved to:", output_file)
    print(combined_usage.head(10))

except Exception as e:
    print(f"⚠️ Error: {e}")