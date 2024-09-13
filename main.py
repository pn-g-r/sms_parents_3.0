import pandas as pd
import requests

# Google Sheets URL
google_sheet_url = "https://docs.google.com/spreadsheets/d/1L4LWXH_72ZdiM83dx45zHvV7W5UoL0_MiV3R4btf41c/gviz/tq?tqx=out:csv&sheet=sharing"
form_data = pd.read_csv(google_sheet_url, header=None)

# Define the correct answers and the corresponding reviews
right_answers = ["5,3", "B", "-10", "59 სმ", "180 კმ", "40, 140, 40", "140", "{1; x}", "60 სმ", "99.9", "კი"]
reviews = ['§2', '§10', '§14', '§20', '§11', '§1', '§14', '§19', '§13', '§3']

# Set up the columns based on index
column_1 = form_data.columns[0]
column_2 = form_data.columns[1]
column_3 = form_data.columns[2]
column_4 = form_data.columns[3]  # This is assumed to be the phone number column
# Columns 5 to 14 are the ones with answers
column_indexes = list(range(4, 14))  # For columns 5 to 14 (0-based index)

# Function to send SMS via the Nando API
def send_sms(api_key, phone_number, message_content, brand_name, no_sms_flag):
    api_url = 'https://nando.ge/api.php'

    # Data to be sent in the POST request
    post_data = {
        'brand_name': brand_name,
        'apikey': api_key,
        'destination': phone_number,
        'content': message_content,
        'no_sms': no_sms_flag
    }

    try:
        response = requests.post(api_url, data=post_data)

        if response.status_code == 200:
            return response.text
        else:
            return f"Error: {response.status_code}"
    except Exception as e:
        return f"Exception occurred: {str(e)}"


# Loop through each row in the DataFrame
for index, row in form_data.iterrows():
    things_to_review = []

    # Loop through columns 5 to 14 (0-indexed as 4 to 13)
    for i, col_index in enumerate(column_indexes):
        try:
            # Compare the row value and right answer as strings
            if str(row[col_index]) != str(right_answers[i]):
                things_to_review.append(str(reviews[i]))  # Ensure review is a string as well
        except ValueError as ve:
            print(f"ValueError for row {index} in column {col_index + 1}: {ve}")

    # API Key and other necessary variables
    api_key = 'c8214ac78ae915da714d50f02449aaf9e02904d4d4b7c3f10d63be97a652b32e'
    brand_name = 'MatMartivad'
    phone_number = str(row[column_4])  # Ensure the phone number is a string
    message_content = f'ტესტის ქულა: {row[column_2]}. რეკომენდაცია - გაიმეოროს პარაგრაფ(ი)ები: {", ".join(things_to_review)}'
    no_sms_flag = 'false'

    # Print message content
    print(f"text {index}: {message_content}")

    # Send the SMS using the send_sms function
    report = send_sms(api_key, phone_number, message_content, brand_name, no_sms_flag)
    print(report)
