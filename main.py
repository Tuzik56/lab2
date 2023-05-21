import requests

city = "Moscow,RU"
appid = "a9a96b909f700dd1b81bb97b1193d4cc"
res_weather = requests.get("http://api.openweathermap.org/data/2.5/weather", params={'q':city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data_weather = res_weather.json()
res_forecast = requests.get("http://api.openweathermap.org/data/2.5/forecast", params={'q':city, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
data_forecast = res_forecast.json()


print("Город:", city)
print("Погодные условия:", data_weather['weather'][0]['description'])
print("Температура:", data_weather['main']['temp'])
print("Минимальная температура:", data_weather['main']['temp_min'])
print("Максимальная температура:", data_weather['main']['temp_max'])
print("Скорость ветра:", data_weather['wind']['speed'])
print("Видимость:", data_weather['visibility'])

print("Прогноз погоды на неделю:")
print("---------------------------------------------")
for i in data_forecast['list']:
    print("Дата <", i['dt_txt'], "> \r\nТемпература <", '{0:+3.0f}'.format(i['main']['temp']), "> \r\nПогодные условия <", i['weather'][0]['description'], "> \r\nСкорость ветра <", i['wind']['speed'], "> \r\nВидимость <", i['visibility'], ">")
    print("---------------------------------------------")
