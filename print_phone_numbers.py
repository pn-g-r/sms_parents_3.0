import pandas as pd

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

# Print the phone numbers as strings without the .0
print("\nPhone numbers from column D as strings (including first row):")
print(phone_numbers)
