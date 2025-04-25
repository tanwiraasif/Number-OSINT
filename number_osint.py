# number_osint.py
# Creator: tanwiraasif

import requests
from bs4 import BeautifulSoup

def get_number_details(phone_number):
    try:
        print("\n[+] Scanning phone number:", phone_number)
        url = f"https://www.findandtrace.com/trace-mobile-number-location/?mobilenumber={phone_number}"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")

        details = {}

        fields = [
            "Mobile Number", "SIM card", "Mobile State", "IMEI number",
            "MAC address", "Connection", "IP address", "Owner Name",
            "Location", "Hometown", "Reference City", "Language",
            "Mobile Locations", "Country", "Tracking History",
            "Tracker Id", "Tower Locations"
        ]

        for field in fields:
            cell = soup.find(string=field)
            if cell:
                value = cell.find_next("td").text.strip()
            else:
                value = "Not found"
            details[field] = value

        return details

    except Exception as e:
        print("[!] Error:", e)
        return None

def display_details(details):
    print("\n======== Phone Number OSINT Result ========")
    for key, value in details.items():
        print(f"{key}: {value}")
    print("===========================================\n")

if __name__ == "__main__":
    print("Phone Number OSINT Tool | Creator: tanwiraasif")

    while True:
        number = input("Enter a phone number (or type 'exit' to quit): ")
        if number.lower() == "exit":
            break
        if not number.isdigit():
            print("[!] Please enter a valid number.")
            continue

        info = get_number_details(number)
        if info:
            display_details(info)
        else:
            print("[!] Failed to fetch details.")
