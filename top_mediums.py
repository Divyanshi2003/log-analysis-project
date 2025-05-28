import pandas as pd

# File paths
input_file = "Commerce_logs.csv"
output_file = "top_mediums.csv"

try:
    print(f"📂 Reading from: {input_file}")
    df = pd.read_csv(input_file)

    if "accessed_Ffom" not in df.columns:
        print("❌ 'accessed_Ffom' column not found.")
    else:
        # Count the most frequent mediums
        top_mediums = df['accessed_Ffom'].value_counts().head(3)

        # Convert to DataFrame
        top_mediums_df = top_mediums.reset_index()
        top_mediums_df.columns = ['medium', 'count']

        # Save to CSV
        top_mediums_df.to_csv(output_file, index=False)

        print(f"✅ Top 3 mediums saved to: {output_file}")
        print("\n📊 Top 3 Mediums:")
        print(top_mediums_df)

except Exception as e:
    print(f"⚠️ Error: {e}")