from weather import Weather

pogoda = Weather("Warszawa")
print(pogoda.status)
print(pogoda.json)


#example of usage
print(pogoda.day[1].temperature)
