import requests
from twilio.rest import Client

account_sid = 'AC40eac0c6acd601078c4d7f53b67d1daf'
auth_token = '28a5445a102e1881a21855ea1cd0eb66'

API = "YOUR_API_KEY"
MY_LAT = 13.082680
MY_LON = 80.270721
URL = f"https://api.openweathermap.org/data/2.5/onecall"
parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=URL, params=parameters)
print(response.status_code)
data = response.json()
weather_id_list = []
for temp in range(12):
    weather_id = data["hourly"][temp]["weather"][0]["id"]
    weather_id_list.append(weather_id)

rain_prone = [True for weather in weather_id_list if weather < 900]
if rain_prone:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an umbrella.",
        from_='REGISTERED_NUMBER',
        to='YOUR_NUMBER'
    )

    print(message.status)
