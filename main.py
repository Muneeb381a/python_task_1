import requests
import os
from dotenv import load_dotenv
import argparse
import json

load_dotenv()

api_key = os.getenv("WEATHER_API_KEY")


parser = argparse.ArgumentParser(description="Provide the city Name")
parser.add_argument("city", help="Enter the city Name")
args = parser.parse_args()
city = args.city


api_url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

response = requests.get(api_url)

data = response.json()
# print(data)

if response.status_code == 200:
    result = {
        "city": city,
        "temperatutre": data["main"]["temp"],
        "wind-speed": data["wind"]["speed"]
    }
    data = response.json()
    print(json.dumps(data, indent=4))


    if os.path.exists("weather.json"):
        with open("weather.json", "r") as file:
            try:
                weather_data = json.load(file)
            except json.JSONDecodeError:
                weather_data = []
    else:
        weather_data = []

    weather_data.append(data)

    with open("weather.json", "w") as file:
        json.dump(weather_data, file, indent=4)
else:
    print(f"Error: {response.status_code}")