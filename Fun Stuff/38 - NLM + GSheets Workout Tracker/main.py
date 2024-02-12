import os
import requests

NUTRITIONIX_API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
NUTRITIONIX_APP_ID = "28bf885a"
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"
exercise_str = input("Tell me which exercise you did: ")

headers = {
    "Content-Type": "application/json",
    "x-app-id": NUTRITIONIX_APP_ID,
    "x-app-key": NUTRITIONIX_API_KEY,
}

post_params = {
    "query": exercise_str
}

response = requests.post(url=URL, headers=headers, json=post_params).json()
print(response)