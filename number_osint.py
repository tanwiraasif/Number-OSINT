import requests

print("Phone Number OSINT Tool | Creator: tanwiraasif")

API_KEY = "f3a0b01d0fe46538a756543fa96f3a58"  # Replace with your full key
BASE_URL = "http://apilayer.net/api/validate"

while True:
    phone_number = input("Enter phone number with country code (or type 'exit' to quit): ")
    if phone_number.lower() == "exit":
        break

    params = {
        'access_key': API_KEY,
        'number': phone_number,
        'country_code': '',
        'format': 1
    }

    print("\n[+] Scanning phone number:", phone_number)
    response = requests.get(BASE_URL, params=params)

    if response.status_code == 200:
        data = response.json()
        print("======= Phone Number OSINT Result =======")
        print("Valid         :", data.get("valid"))
        print("Number        :", data.get("international_format"))
        print("Local Format  :", data.get("local_format"))
        print("Country       :", data.get("country_name"))
        print("Location      :", data.get("location"))
        print("Carrier       :", data.get("carrier"))
        print("Line Type     :", data.get("line_type"))
        print("========================================\n")
    else:
        print("Error: Could not retrieve data.")
