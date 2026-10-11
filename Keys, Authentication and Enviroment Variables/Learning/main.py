import requests
# from twilio.rest import Client | This is for SMS function, but i dont have an account for it

api_key = "f0b1b4713efe710b8f77db09b6064b67"
# when we set our enviroment key in terminal, we will use this line of code instead of typing our real api key inside
# our program, so our api key will not get leaked and people cannot abuse and use it
# api_key = os.environ.get("weather_api_key")

# this is for SMS portion
# account_sid = "SID"
# auth_token = "auth_token"
# auth_token = os.environ.get("AUTH_TOKEN"), same as above, save as enviroment key

parameters = {
    "lat" : 1.45338,
    "lon" : 103.81583,
    "appid" : api_key,
    "cnt" : 4
}

response = requests.get("https://api.openweathermap.org/data/2.5/forecast", params=parameters)
response.raise_for_status()
# print(response.status_code)
data = response.json()

def will_rain():
    rain = False
    for weather_condition in data["list"]:
        if weather_condition["weather"][0]["id"] < 700 :
            rain = True
    if rain :
        print("It is going to rain. Bring an umbrella!")
    # this for sending SMS function
    # client = Client(account_sid, auth_token)
    # message = client.messages.create(
    #     body = "It will rain, bring an umbrella!",
    #     from_ = "twilio phone number",
    #     to = "my phone number"
    # )
    # print(message.status)
    else:
        print("No rain expected.")
will_rain()