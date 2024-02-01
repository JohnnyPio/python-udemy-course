import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
longitude = data.get("iss_position").get("longitude")
latitude = data.get("iss_position").get("latitude")

iss_pos = (longitude, latitude)
print(iss_pos)
