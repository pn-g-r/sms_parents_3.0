import re

# Sample input with non-digit characters and phone numbers
phone = "1234*&^567@$89 asjfas jaa^(#%) 122112211         ///..  "

# Step 1: Remove all non-digit characters
digits_only = re.sub(r'\D', '', phone)  # Replace all non-digits with an empty string

# Step 2: Split the resulting string into chunks of 9 digits
split_phones = [digits_only[i:i+9] for i in range(0, len(digits_only), 9)]

# Print the result
print(split_phones)