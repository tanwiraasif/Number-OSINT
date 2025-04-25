import requests
from bs4 import BeautifulSoup
import re

def trace_number(phone_number):
    url = "https://calltracer.in"
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:133.0) Gecko/20100101 Firefox/133.0",
        "Content-Type": "application/x-www-form-urlencoded",
    }
    payload = {"country": "IN", "q": phone_number}

    try:
        response = requests.post(url, headers=headers, data=payload)
        if response.status_code == 200:
            soup = BeautifulSoup(response.text, "html.parser")
            details = {}
            try:
                details["📞 Number"] = phone_number
                details["❗️ Complaints"] = soup.find(text="Complaints").find_next("td").text
                details["👤 Owner Name"] = soup.find(text="Owner Name").find_next("td").text
                details["📶 SIM card"] = soup.find(text="SIM card").find_next("td").text
                details["📍 Mobile State"] = soup.find(text="Mobile State").find_next("td").text
                details["🔑 IMEI number"] = soup.find(text="IMEI number").find_next("td").text
                details["🌐 MAC address"] = soup.find(text="MAC address").find_next("td").text
                details["⚡️ Connection"] = soup.find(text="Connection").find_next("td").text
                details["🌍 IP address"] = soup.find(text="IP address").find_next("td").text
                details["🏠 Owner Address"] = soup.find(text="Owner Address").find_next("td").text
                details["🏘 Hometown"] = soup.find(text="Hometown").find_next("td").text
                details["🗺 Reference City"] = soup.find(text="Refrence City").find_next("td").text
                details["👥 Owner Personality"] = soup.find(text="Owner Personality").find_next("td").text
                details["🗣 Language"] = soup.find(text="Language").find_next("td").text
                details["📡 Mobile Locations"] = soup.find(text="Mobile Locations").find_next("td").text
                details["🌎 Country"] = soup.find(text="Country").find_next("td").text
                details["📜 Tracking History"] = soup.find(text="Tracking History").find_next("td").text
                details["🆔 Tracker Id"] = soup.find(text="Tracker Id").find_next("td").text
                details["📶 Tower Locations"] = soup.find(text="Tower Locations").find_next("td").text
            except Exception:
                return "⚠️ Error: Unable to extract all details. The format may have changed."
            return details
        else:
            return f"⚠️ Failed to fetch data. HTTP Status Code: {response.status_code}"
    except Exception as e:
        return f"❌ An error occurred: {str(e)}"

def main():
    print("\n🔍 Welcome to Number OSINT Tool 🔍")
    while True:
        phone_number = input("\nEnter a phone number (or type 'exit' to quit): ").strip()
        if phone_number.lower() == "exit":
            print("Goodbye!")
            break
        print(f"\n🔎 Searching for {phone_number}...\n")
        result = trace_number(phone_number)
        if isinstance(result, dict):
            for key, value in result.items():
                print(f"{key}: {value}")
        else:
            print(result)

if __name__ == "__main__":
    main()
