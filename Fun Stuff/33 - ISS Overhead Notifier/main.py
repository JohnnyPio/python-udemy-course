import requests
from datetime import datetime

MY_LAT = 40.645270
MY_LONG = -73.981180
MY_TIMEZONE = "America/New_York"

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])


# Your position is within +5 or -5 degrees of the ISS position.
def iss_nearby():
    if (MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and
            MY_LONG - 5 <= iss_longitude <= MY_LONG + 5):
        return True


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
    "tzid": MY_TIMEZONE
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()
print(sunrise)
print(sunset)
print(time_now)

# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
# BONUS: run the code every 60 seconds.
