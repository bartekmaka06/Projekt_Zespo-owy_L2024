import os
import requests
from datetime import date, timedelta, datetime
from dateutil import tz
import pickle


class Weather:

    def __init__(self, city):
        self.day = []
        self.city = city
        self.status = self.get_weather()


    def get_weather(self):
        self.day.clear()

        if self.download_weather() == "success":
            with open(f'{self.city}.pkl', 'wb') as f:
                pickle.dump(self.day, f)
            return "ok_online"
        else:
            if os.path.isfile(f'{self.city}.pkl'):
                with open(f'{self.city}.pkl', 'rb') as f:
                    self.day = pickle.load(f)
                return "ok_offline"
            else:
                return "nok"



    def download_weather(self):
        API_KEY = '5cb00ebacb888af1ed92bedb4ce335d7'

        url_30 = f'https://pro.openweathermap.org/data/2.5/forecast/climate?q={self.city}&units=metric&appid={API_KEY}'
        url_now = f'https://api.openweathermap.org/data/2.5/weather?q={self.city}&units=metric&appid={API_KEY}'


        try:
            res_now = requests.get(url_now)
            res_30 = requests.get(url_30)
        except requests.ConnectionError:
            return "fail"



        presentday = date.today()
        download_time = datetime.now()
        res_dict = res_30.json()
        res_dict_now = res_now.json()


        for i in range(0, len(res_dict["list"])):
            if i == 0:
                #pozmieniac aby dane aktualne byly brane z prognozy aktualnej
                self.day.append(Day(str(presentday + timedelta(i)),
                                    download_time,
                                    res_dict_now["main"]["temp"],
                                    res_dict_now["main"]["temp_min"],
                                    res_dict_now["main"]["temp_max"],
                                    res_dict_now["weather"][0]["icon"],
                                    res_dict_now["main"]["pressure"],
                                    res_dict_now["main"]["humidity"],
                                    res_dict_now["weather"][0]["description"],
                                    res_dict_now["sys"]["sunrise"],
                                    res_dict_now["sys"]["sunset"],
                                    res_dict_now["wind"]["speed"]))
            else:
                self.day.append(Day(str(presentday + timedelta(i)),
                                    download_time,
                                    res_dict["list"][i]["temp"]["day"],
                                    res_dict["list"][i]["temp"]["min"],
                                    res_dict["list"][i]["temp"]["max"],
                                    res_dict["list"][i]["weather"][0]["icon"],
                                    res_dict["list"][i]["pressure"],
                                    res_dict["list"][i]["humidity"],
                                    res_dict["list"][i]["weather"][0]["description"],
                                    res_dict["list"][i]["sunrise"],
                                    res_dict["list"][i]["sunset"],
                                    res_dict["list"][i]["speed"]))

        return "success"




class Day:

    def __init__(self, date, download_date, temperature_avg, temperature_min, temperature_max, overall_icon, pressure, humidity,
                 description, sunrise,
                 sunset, wind_speed):
        self.date = date
        self.download_date = download_date
        self.temperature_avg = temperature_avg
        self.temperature_min = temperature_min
        self.temperature_max = temperature_max
        self.overall_icon = overall_icon
        self.pressure = pressure
        self.humidity = humidity
        self.description = description
        self.sunrise_utc = datetime.utcfromtimestamp(sunrise).replace(tzinfo=tz.tzutc())
        self.sunset_utc = datetime.utcfromtimestamp(sunset).replace(tzinfo=tz.tzutc())
        self.wind_speed = wind_speed
        self.sunrise = self.sunrise_utc.astimezone(tz.tzlocal()).strftime('%H:%M')
        self.sunset = self.sunset_utc.astimezone(tz.tzlocal()).strftime('%H:%M')

