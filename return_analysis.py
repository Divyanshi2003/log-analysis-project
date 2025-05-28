import pandas as pd

# File path
input_file = "Commerce_logs.csv"

try:
    # Load the data
    df = pd.read_csv(input_file)

    # Total number of orders
    total_orders = len(df)

    # Filter returned orders
    returned_orders = df[df['returned'].str.lower() == 'yes']
    num_returned = len(returned_orders)

    # Calculate percentage
    percent_returned = (num_returned / total_orders) * 100

    # Calculate total return value
    total_returned_value = returned_orders['returned_amount'].sum()

    # Display results
    print("📦 Return Analysis:")
    print(f"• Total Orders: {total_orders}")
    print(f"• Returned Orders: {num_returned}")
    print(f"• % of Orders Returned: {percent_returned:.2f}%")
    print(f"• Total Returned Amount: ${total_returned_value:,.2f}")

except Exception as e:
    print(f"⚠️ Error: {e}")