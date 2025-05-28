import pandas as pd

# Load the original log CSV
input_file = "Commerce_logs.csv"
output_file = "ip_frequency.csv"

try:
    # Read the CSV into a DataFrame
    df = pd.read_csv(input_file)

    # Count frequency of each IP
    ip_counts = df['ip'].value_counts()

    # Convert the Series to a DataFrame and reset index
    ip_freq_df = ip_counts.reset_index()
    ip_freq_df.columns = ['ip', 'count']  # Rename columns

    # Save to CSV
    ip_freq_df.to_csv(output_file, index=False)

    print(f"✅ IP frequency analysis complete. Results saved to: {output_file}")
    print(ip_freq_df.head())

except Exception as e:
    print(f"⚠️ Error: {e}")