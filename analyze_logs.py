import csv

print("Starting log analysis...")

try:
    with open("Commerce_logs.csv", newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            print(row)
except Exception as e:
    print(f"⚠️ Error: {e}")