import requests
import json
class Weather:
  def __init__(self, city):
    self.json = None
    self.city = city
    self.status = self.get_weather()

  def get_weather(self):
    API_KEY = '5cb00ebacb888af1ed92bedb4ce335d7'
    url = f'https://pro.openweathermap.org/data/2.5/forecast/climate?q={self.city}&appid={API_KEY}'
    res = requests.get(url)
    self.json = res.json()
    return res



