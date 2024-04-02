import requests
import json
class Weather:
  def __init__(self, city):
    self.day = []
    self.json = None
    self.city = city
    self.status = self.get_weather()

  def get_weather(self):
    API_KEY = '5cb00ebacb888af1ed92bedb4ce335d7'
    url = f'https://pro.openweathermap.org/data/2.5/forecast/climate?q={self.city}&appid={API_KEY}'
    res = requests.get(url)
    self.json = res.json()
    #tutaj dodac petle ktora utworzy tabele dni i przypisze im pogody
    #self.days.append(Day("15"))
    return res



class Day:
  def __init__(self,temperature_avg,temperature_min,temperature_max,overall_icon,pressure,humidity,rain,sunrise,
               sunset,wind_speed):
    self.temperature_avg = temperature_avg
    self.temperature_min = temperature_min
    self.temperature_max = temperature_max
    self.overall_icon = overall_icon
    self.pressure = pressure
    self.humidity = humidity
    self.rain = rain
    self.sunrise = sunrise
    self.sunset = sunset
    self.wind_speed = wind_speed



