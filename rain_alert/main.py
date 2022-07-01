
import requests
import os
from twilio.rest import Client

account_sid = "AC3a14ccd714348a8563e3e61d726016ad"
auth_token = "47964cb81ffdfdd93ee850860c8bd73c"

parameters = {
   "lat": 23.259933,
   "lon": 77.412613,
   "appid": "2d997b42ff29bb4978eea3bd2f1b126e",
   "exclude":"current,minutely,daily"
}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params = parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]
Will_rain = False

for hour_data in weather_slice:
   condition_code = hour_data["weather"][0]["id"]
   if int(condition_code) < 700:
      will_rain = True

if will_rain:
   client = Client(account_sid, auth_token)
   message = client.messages \
      .create(
      body="Hi, My first message from Twilio.",
      from_='+13082808352',
      to='+919821085099'
   )

   print(message.status)


#print(weather_data["hourly"][0]["weather"][0]["id"])


