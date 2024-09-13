import pandas as pd
import re

# Read the Google Sheet as a CSV
url = "https://docs.google.com/spreadsheets/d/1jH904oVra4Oe20zNbSVkgmtmVUzIiXeTtkiIzICh2ww/gviz/tq?tqx=out:csv&sheet=Sheet1"
df = pd.read_csv(url)

# Display the first few rows to check the structure
print("First few rows of the sheet:")
print(df.head())

# Assuming column D is the 4th column (index 3)
# Convert the column to strings, remove .0, and remove NaN
phone_numbers = df.iloc[:, 3].dropna().apply(lambda x: str(x).replace('.0', '').strip())

# Reset the index to keep everything in order starting from the first row
phone_numbers.index = range(1, 1 + len(phone_numbers))

# Iterate through the phone numbers to check for multiple phone numbers in a row
for idx, phone in phone_numbers.items():
    # Use re.split to split on comma or any amount of spaces
    split_phones = re.split(r'[,\s]+', phone.strip())  # Split on comma and/or spaces
    
    # Remove any empty strings that might have been created by splitting
    split_phones = [p for p in split_phones if p]

    if len(split_phones) > 1:
        # If there are multiple phone numbers, print both phone numbers
        print(f"\nRow {idx}:")
        print(f"Phone number 1: {split_phones[0]}")
        print(f"Phone number 2: {split_phones[1]}")
    else:
        # Only one phone number in the row, print it
        print(f"\nRow {idx}:")
        print(f"Phone number: {phone}")
