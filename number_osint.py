import requests
import phonenumbers

# Cool ASCII art for the title
print(r"""
=======================================================================
   ____  _   _  ____  _   _  _____  _____  _____  ____  ____  _____
  /  _ \/  / \/  _ \/  / \/  __/ /  __/ /  __/ /  _ \/  _ \/  __/
  | / \||  / || / \||  / ||  \  |  \  |  \  | / \|| / \||  \/|
  | \_/||  \_/| \_/||  \_/|  /_ |  /_ |  /_ | \_/|| \_/||    / 
  \____/\____/\____/\____/\____\\____\\____\\____/\____/|_|_\|
  NUMBER OSINT - Created by TANWIR AASIF
=======================================================================
""")

# Replace 'your_actual_api_key' with your Numverify API key
API_KEY = ""  # Insert your Numverify API key here
BASE_URL = "https://apilayer.net/api/validate"

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
        print("======= PHONE OSINT RESULTS =======")
        print(f"Valid         : {data.get('valid', 'N/A')}")
        print(f"Number        : {data.get('international_format', 'N/A')}")
        print(f"Local Format  : {data.get('local_format', 'N/A')}")
        print(f"Country       : {data.get('country_name', 'N/A')}")
        print(f"Location      : {data.get('location', 'N/A')}")
        print(f"Carrier       : {data.get('carrier', 'N/A')}")
        print(f"Line Type     : {data.get('line_type', 'N/A')}")
        print("==================================\n")
    else:
        print("Error: Invalid phone number according to the API response.")

def main():
    while True:
        phone_number = input("Enter phone number with country code (or type 'exit' to quit): ").strip()
        if phone_number.lower() in ("exit", "quit", "q"):
            print("Exiting... Stay stealthy! 👾")
            break

        if len(phone_number) > 50:  # Basic input length check
            print("Error: Phone number is too long. Keep it legit!")
            continue

        if not is_valid_phone_number(phone_number):
            print("Error: Invalid phone number format. Try again, hacker!")
            continue

        print("\n[+] Scanning phone number like a pro:", phone_number)
        data = get_phone_info(phone_number)
        display_phone_info(data)

if __name__ == "__main__":
    main()
