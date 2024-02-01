import requests
import datetime as dt

MY_LAT = 40.645270
MY_LONG = -73.981180
MY_TIMEZONE = "America/New_York"

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# longitude = data.get("iss_position").get("longitude")
# latitude = data.get("iss_position").get("latitude")
#
# iss_pos = (longitude, latitude)
# print(iss_pos)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": MY_TIMEZONE
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data.get("results").get("sunrise")
sunrise_hour = sunrise.split("T")[1].split(":")[0]
sunset = data.get("results").get("sunset")
sunset_hour = sunset.split("T")[1].split(":")[0]


time_now = dt.datetime.now()
hour_now = time_now.hour
print(sunrise_hour)
print(sunset_hour)
print(hour_now)
