import requests
import phonenumbers  # You can install this via pip install phonenumbers

print("Phone Number OSINT Tool | Creator: tanwiraasif")

API_KEY = "f3a0b01d0fe46******"  # Replace with your full key
BASE_URL = "http://apilayer.net/api/validate"

def is_valid_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

while True:
    phone_number = input("Enter phone number with country code (or type 'exit' to quit): ")
    if phone_number.lower() == "exit":
        break

    # Check if the phone number is valid
    if not is_valid_phone_number(phone_number):
        print("Error: Invalid phone number format. Please try again.")
        continue

    # Automatically detect country code if not provided
    try:
        parsed_number = phonenumbers.parse(phone_number)
        country_code = phonenumbers.region_code_for_number(parsed_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        country_code = ''  # Empty if country code is not detected

    params = {
        'access_key': API_KEY,
        'number': phone_number,
        'country_code': country_code,
        'format': 1
    }

    print("\n[+] Scanning phone number:", phone_number)
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        if data.get("valid") == "true":
            print("======= Phone Number OSINT Result =======")
            print(f"Valid         : {data.get('valid')}")
            print(f"Number        : {data.get('international_format')}")
            print(f"Local Format  : {data.get('local_format')}")
            print(f"Country       : {data.get('country_name')}")
            print(f"Location      : {data.get('location')}")
            print(f"Carrier       : {data.get('carrier')}")
            print(f"Line Type     : {data.get('line_type')}")
            print("========================================\n")
        else:
            print("Error: Invalid phone number according to the API response.")
    else:
        print("Error: Could not retrieve data. API returned status code", response.status_code)
