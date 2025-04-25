import requests
import phonenumbers
import os
from dotenv import load_dotenv

print("Phone Number OSINT Tool | Creator: tanwiraasif")

# Load API key from environment variable
load_dotenv()
API_KEY = os.getenv("NUMVERIFY_API_KEY")
if not API_KEY:
    raise ValueError("API key not found. Set NUMVERIFY_API_KEY in .env file.")

BASE_URL = "https://apilayer.net/api/validate"  # Use HTTPS explicitly

def is_valid_phone_number(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        return phonenumbers.is_valid_number(parsed_number)
    except phonenumbers.phonenumberutil.NumberParseException:
        return False

def get_phone_info(phone_number):
    try:
        parsed_number = phonenumbers.parse(phone_number)
        country_code = phonenumbers.region_code_for_number(parsed_number) or ""
    except phonenumbers.phonenumberutil.NumberParseException:
        country_code = ""

    params = {
        "access_key": API_KEY,
        "number": phone_number,
        "country_code": country_code,
        "format": 1,
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)
        response.raise_for_status()  # Raise exception for non-200 status codes
        return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Error: Failed to retrieve data from API: {e}")
        return None

def display_phone_info(data):
    if not data:
        return

    if data.get("valid", False):
        print("======= Phone Number OSINT Result =======")
        print(f"Valid         : {data.get('valid', 'N/A')}")
        print(f"Number        : {data.get('international_format', 'N/A')}")
        print(f"Local Format  : {data.get('local_format', 'N/A')}")
        print(f"Country       : {data.get('country_name', 'N/A')}")
        print(f"Location      : {data.get('location', 'N/A')}")
        print(f"Carrier       : {data.get('carrier', 'N/A')}")
        print(f"Line Type     : {data.get('line_type', 'N/A')}")
        print("========================================\n")
    else:
        print("Error: Invalid phone number according to the API response.")

def main():
    while True:
        phone_number = input("Enter phone number with country code (or type 'exit' to quit): ").strip()
        if phone_number.lower() in ("exit", "quit", "q"):
            print("Exiting...")
            break

        if len(phone_number) > 50:  # Basic input length check
            print("Error: Phone number is too long. Please try again.")
            continue

        if not is_valid_phone_number(phone_number):
            print("Error: Invalid phone number format. Please try again.")
            continue

        print("\n[+] Scanning phone number:", phone_number)
        data = get_phone_info(phone_number)
        display_phone_info(data)

if __name__ == "__main__":
    main()
