from weather import Weather


pogoda = Weather("Łódź")
#print(pogoda.status)
#pogoda.refresh()


#example of usage
print(pogoda.day[0].temperature_avg)
