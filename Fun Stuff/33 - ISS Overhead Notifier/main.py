import smtplib
import requests
import datetime as dt
import time
import sched

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

time_now = dt.datetime.now()
hour_now = time_now.hour
print(sunrise)
print(sunset)
print(hour_now)


def is_night():
    if hour_now > sunset or hour_now < sunrise:
        return True


# If the ISS is close to my current position
# and it is currently dark
# Then send me an email to tell me to look up.
def notify_me():
    if iss_nearby() and is_night():
        email = "john.s.piotrowski@gmail.com"
        password = "mgqw gtcc fame vnjd"

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=email, password=password)
            connection.sendmail(
                from_addr=email,
                to_addrs=email,
                msg=f"Subject: ISS Overhead, Look Up!! \n\n The ISS is overhead!"
            )


# BONUS: run the code every 60 seconds.
my_scheduler = sched.scheduler(time.time, time.sleep)
my_scheduler.enter(60, 1, notify_me)
my_scheduler.run()
