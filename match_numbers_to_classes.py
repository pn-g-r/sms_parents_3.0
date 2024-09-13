import pandas as pd

# Read the Google Sheet as a CSV
url = "https://docs.google.com/spreadsheets/d/1jH904oVra4Oe20zNbSVkgmtmVUzIiXeTtkiIzICh2ww/gviz/tq?tqx=out:csv&sheet=Sheet1"
df = pd.read_csv(url, dtype=str)  # Read everything as string to preserve leading zeros

# Display the first few rows to check the structure
print("First few rows of the sheet:")
print(df.head())

# Check if any row in column D matches '593398370', and print the corresponding value in column F
matching_rows = df[df.iloc[:, 3] == '593398370']  # Column D is the 4th column (index 3)

if not matching_rows.empty:
    print("\nValue in column F for the row where column D is '593398370':")
    print(matching_rows.iloc[:, 5])  # Column F is the 6th column (index 5)
else:
    print("\nNo rows found where column D is '593398370'.")
