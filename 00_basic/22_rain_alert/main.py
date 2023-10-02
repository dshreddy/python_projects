import requests
from twilio.rest import Client
import os

#                                             WEATHER API CALL SETUP

# Weather data provider API documentation : https://openweathermap.org/api/one-call-3#current
API_endpoint = "https://api.openweathermap.org/data/2.5/onecall"
API_key = os.getenv("OWM_API_KEY")

#  Kanjikode location from https://www.latlong.net/
lat = 10.797260
lon = 76.739677

parameters = {
    "lat": lat,
    "lon": lon,
    "appid": API_key,
    "exclude": {"current,minutely,daily"}
}

response = requests.get(API_endpoint, params=parameters)
response.raise_for_status()

#                                 CHECKING IF IT RAINS IN NEXT 12 HRS

# Weather ID vs climate : https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
will_rain = False
hourly_prediction_list = response.json()["hourly"]
for i in range(0, 12):
    weather_id = hourly_prediction_list[i]['weather'][0]['id']
    if int(weather_id) <= 700:
        will_rain = True
        break


#                                                   SMS

account_sid = 'AC69f2302898b8b8a658de3d153d83cdc0'
auth_token = os.getenv("AUTH_TKN")
client = Client(account_sid, auth_token)

if will_rain:
    message = client.messages.create(
      from_='+18066028125',
      to='+918106205291',
      body="It will rain, bring an Umbrella"
    )
    print(message.status)
