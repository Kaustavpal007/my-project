import requests
import sys

API_KEY = "5Sfc3mhadUEmQlZGjW018FB9ewqY1qkQQcZmJsMp"

def apod():
    url = f"https://api.nasa.gov/planetary/apod?api_key={API_KEY}"
    data = requests.get(url).json()

    print("\nNASA Astronomy Picture of the Day")
    print("Title:", data["title"])
    print("Date:", data["date"])
    print("Image:", data["url"])

def iss():
    url = "http://api.open-notify.org/iss-now.json"
    data = requests.get(url).json()

    print("\nISS Current Location")
    print("Latitude:", data["iss_position"]["latitude"])
    print("Longitude:", data["iss_position"]["longitude"])

def main():
    if len(sys.argv) < 2:
        print("Usage: utility-life [apod|iss]")
        return

    cmd = sys.argv[1]

    if cmd == "apod":
        apod()
    elif cmd == "iss":
        iss()
    else:
        print("Unknown command")
