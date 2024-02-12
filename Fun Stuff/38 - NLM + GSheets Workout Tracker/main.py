import datetime as dt
import os
import requests

# Get the Data from Nutritionix
NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_APP_ID = "28bf885a"
NUTRITIONIX_URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
SHEETY_URL = "https://api.sheety.co/085e5a52572f220cbc60ab7f73db0177/myWorkouts/workouts"

user_input = input("Tell me which exercise you did: ")
headers = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

post_params = {
    "query": user_input
}

nutrition_response = requests.post(url=NUTRITIONIX_URL, headers=headers, json=post_params)
response_json = nutrition_response.json()
exercises = response_json.get("exercises")

# Push that data to Sheety
SHEETY_AUTH = os.environ.get("SHEETY_AUTH")
sheety_headers = {
    "Authorization": SHEETY_AUTH
}

for _ in exercises:
    date = dt.datetime.now().date().strftime("%Y%m%d")
    time = dt.datetime.now().time().strftime("%X")
    exercise = _.get("user_input")
    duration = _.get("duration_min")
    calories = _.get("nf_calories")
    json = {
        "workout": {
            "date": date,
            "time": time,
            "exercise": exercise,
            "duration (minutes)": duration,
            "calories": calories
        }
    }
    # Send that data to Sheety
    sheety_response = requests.post(url=SHEETY_URL, json=json, headers=sheety_headers)
