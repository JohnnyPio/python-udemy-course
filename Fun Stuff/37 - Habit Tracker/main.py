import requests
import os
from datetime import datetime

USERNAME = "jspiotrowski"
TOKEN = os.environ.get("PIXELA_TOKEN")
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_params = {
    "id": GRAPH_ID,
    "name": "Phoebe Walks",
    "unit": "walks",
    "type": "int",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# Posting some data
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()
TODAY = today.strftime("%Y%m%d")

pixel_params = {
    "date": TODAY,
    "quantity": "3",
}

# response = requests.post(url=pixel_creation_endpoint, json=pixel_params, headers=headers)
# print(response.text)

pixel_put_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{TODAY}"

put_params = {
    "quantity": "3",
}

response = requests.put(url=pixel_put_endpoint, json=put_params, headers=headers)
print(response.text)
