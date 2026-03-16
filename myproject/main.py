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


def mars():
    url = f"https://api.nasa.gov/mars-photos/api/v1/rovers/curiosity/photos?sol=1000&api_key={API_KEY}"
    data = requests.get(url).json()

    if data["photos"]:
        photo = data["photos"][0]
        print("\nMars Rover Photo")
        print("Rover:", photo["rover"]["name"])
        print("Camera:", photo["camera"]["full_name"])
        print("Image:", photo["img_src"])
    else:
        print("No photos found.")


def search(query):
    url = f"https://images-api.nasa.gov/search?q={query}"
    data = requests.get(url).json()

    items = data["collection"]["items"]

    if items:
        print("\nNASA Image Search Results")
        for item in items[:3]:
            print("-", item["data"][0]["title"])
    else:
        print("No results found.")


def main():
    if len(sys.argv) < 2:
        print("Usage: utility-life [apod|iss|mars|search]")
        return

    cmd = sys.argv[1]

    if cmd == "apod":
        apod()
    elif cmd == "iss":
        iss()
    elif cmd == "mars":
        mars()
    elif cmd == "search":
        if len(sys.argv) < 3:
            print("Usage: utility-life search <keyword>")
        else:
            search(sys.argv[2])
    else:
        print("Unknown command")


if __name__ == "__main__":
    main()
