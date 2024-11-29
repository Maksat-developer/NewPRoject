import requests
import telebot
from config import open_weather_token
from pprint import pprint as pp

# bot = telebot.TeleBot("5070463877:AAFn362g_K88-v46PM7NG5lGQ9Q5AH3iVjU")


def get_weather(city, open_weather_token):
    try:
        r = requests.get(
            f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={open_weather_token}&units=metric"
        )
        data = r.json()
        # pp(data)

        city = data["name"]
        cur_wether = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind = data["wind"]["speed"]
        print(f"Погода в городе: {city}\nТемпература: {cur_wether}\n Влажность: {humidity}\n Скорость ветра: {wind}")







    except Exception as ex:
        pp(ex)
        pp("Check city name")


def main():
    city = input("Введите город: ")
    get_weather(city, '2e78a8ab6a6cff19596387f97bba81d4')


if __name__ == '__main__':
    main()