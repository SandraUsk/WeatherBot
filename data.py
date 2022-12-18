import json
import datetime
from urllib.request import urlopen

token="5937325752:AAHVYuRtSegWKLpUelqQebS8IESTG6xbo_M"

weatherapi_key = "b420ec754a1d80a3ae9de4e0235dae9b"

msk_id = "524901"


def get_weather(city_id):
    weatherapi_call = "http://api.openweathermap.org/data/2.5/forecast?id=" + city_id + "&appid=" + weatherapi_key
    weatherapi_response = urlopen(weatherapi_call).read()
    weather_dict = json.loads(weatherapi_response)
    t_real = str(round(int(weather_dict['list'][0]['main']['temp'])-273,15))
    t_feel = str(round(int(weather_dict['list'][0]['main']['feels_like'])-273,15))
    humidity = str(weather_dict['list'][0]['main']['humidity'])
    wind_speed = str(round(weather_dict['list'][0]['wind']['speed']))
    weather = "Температура воздуха сейчас " + t_real + " C (ощущается как " + t_feel + " C). Влажность - " + humidity + "%. Скорость ветра - " + wind_speed + " м/c."
    return weather

def get_suntime(city_id):
    weatherapi_call = "http://api.openweathermap.org/data/2.5/forecast?id=" + city_id + "&appid=" + weatherapi_key
    weatherapi_response = urlopen(weatherapi_call).read()
    weather_dict = json.loads(weatherapi_response)
    sunrise = str(((weather_dict['city']['sunrise'] + weather_dict['city']['timezone']) % (24*60*60)) // 3600) + ":" + str((((weather_dict['city']['sunrise'] + weather_dict['city']['timezone']) % (24*60*60)) // 60) % 60)
    sunset = str(((weather_dict['city']['sunset'] + weather_dict['city']['timezone']) % (24*60*60)) // 3600) + ":" + str((((weather_dict['city']['sunset'] + weather_dict['city']['timezone']) % (24*60*60)) // 60) % 60)
    s = "Восход солнца в " + str(sunrise) + ", заход - в " + str(sunset)
    return s
