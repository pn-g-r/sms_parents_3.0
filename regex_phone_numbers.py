# number validation

import re

def normalize_phone_number(phone: str) -> str:
    # Use regex to replace any non-digit characters with an empty string
    return re.sub(r'\D', '', phone)

# Example usage
phone_with_dashes = "56-8 0*9 00 23-3"
normalized_phone = normalize_phone_number(phone_with_dashes)

print(normalized_phone)  # Outputs: 568002233
