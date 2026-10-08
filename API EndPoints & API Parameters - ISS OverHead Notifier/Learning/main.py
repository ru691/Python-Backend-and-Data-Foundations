import requests
from datetime import datetime
#
# response = requests.get(url = "http://api.open-notify.org/iss-now.json")
# # response.raise_for_status()
#
# response_json = response.json()
#
# longitude = response_json["iss_position"]["longitude"]
# latitude = response_json["iss_position"]["latitude"]
# iss_position = (longitude, latitude)
# print(iss_position)

lat = 1.444016
long = 103.817117
parameters = {
    "lat" : lat,
    "lng" : long,
    "formatted" : 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
sunrise_sunset = (sunrise, sunset)
print(sunrise)
print(sunset)
print(sunrise_sunset)
time_now = datetime.now()
print(time_now.hour)