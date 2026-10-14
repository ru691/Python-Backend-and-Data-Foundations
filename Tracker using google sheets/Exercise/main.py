import requests
from datetime import datetime
import os

GENDER = "male"
WEIGHT_KG = 73
HEIGHT_CM = 173
AGE = 25

username = os.environ["username"]
password = os.environ["password"]
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]


EXERCISE_ENDPOINT = "https://app.100daysofpython.dev/v1/nutrition/natural/exercise"
SERVER_STATUS_ENDPOINT = "https://app.100daysofpython.dev/healthz"
SHEETY_POST_ENDPOINT = os.environ["SHEETY_POST_ENDPOINT"]

data = {
    "query" : input("Exercise description: "),
    "weight_kg" : WEIGHT_KG,
    "height_cm" : HEIGHT_CM,
    "age" : AGE,
    "gender" : GENDER,
}

# Supported activities:
#
#     Running/Jogging - "ran for 30 minutes", "jogged 2 miles"
#     Swimming - "swam for 1 hour", "swimming laps"
#     Walking - "walked 3 miles", "brisk walk 45 min"
#     Cycling - "biked for 1 hour", "rode bike 10 miles"
#     Weightlifting - "lifted weights 45 min", "weight training"

HEADERS = {
    "Content-type": "application/json",
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

response = requests.post(url =EXERCISE_ENDPOINT, headers=HEADERS, json=data)
response.raise_for_status()
result = response.json()
# print(result)

# CHECK SERVER STATUS
# status = requests.get(SERVER_STATUS_ENDPOINT)
# print(status)

today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
# print(now_time)

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout" :{
            "date" : today_date,
            "time" : now_time,
            "exercise" : exercise["name"].title(),
            "duration" : exercise["duration_min"],
            "calories" : exercise["nf_calories"],
        }
    }
    sheet_response = requests.post(url =SHEETY_POST_ENDPOINT, json=sheet_inputs, auth=(username, password))
    sheet_response.raise_for_status()
    print(sheet_response.text)

# to check the sheety API structure to use Date or date, Time or time so on
# check = requests.get(url = SHEETY_POST_ENDPOINT)
# print(check.text)