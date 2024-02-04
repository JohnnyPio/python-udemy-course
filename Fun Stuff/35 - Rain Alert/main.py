import requests

API_KEY = "2ecab42cfaf25fd97f8fe4d2acba44cf"
MY_LAT = 40.485489
MY_LONG = -106.833557

response = requests.get(f"https://api.openweathermap.org/data/2.5/forecast?lat={MY_LAT}&lon={MY_LONG}&appid={API_KEY}").json
print(response)