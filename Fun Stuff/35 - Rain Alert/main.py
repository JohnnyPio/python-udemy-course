import requests

API_KEY = "2ecab42cfaf25fd97f8fe4d2acba44cf"
WEATHER_ENDPOINT = "https://api.openweathermap.org/data/2.5/forecast"

weather_params = {
    "lat": 40.485489,
    "lon": -106.833557,
    "appid": API_KEY,
}


response = requests.get(WEATHER_ENDPOINT, params=weather_params).json()
print(response)