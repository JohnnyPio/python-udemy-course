import requests
import os

API_KEY = os.environ.get("OWM_API_KEY")
WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": 40.485489,
    "lon": -106.833557,
    "cnt": 4,
    "units": "imperial",
    "appid": API_KEY,
}

response = requests.get(WEATHER_ENDPOINT, params=weather_params)
response.raise_for_status()
weather_data = response.json()

# Check for rain
ids = []
for item in weather_data.get("list"):
    weather_list_item = item.get("weather")
    for hourly_weather in weather_list_item:
        hourly_id = hourly_weather.get("id")
        ids.append(hourly_id)

if [i for i in ids if i < 600]:
    print("Bring an umbrella")
else:
    print("You good")
