from weather import Weather


pogoda = Weather("Łódź")
#print(pogoda.status)
# jeśli jest internet i udało się pobrać pogodę najnowszą: "ok_online" - zmienne są tworzone w oparciu o dane online i aktualizowany jest zestaw dni w pliku
# jeśli nie ma internetu/nie udało się pobrać danych ale jest plik: "ok_offline" - zmienne są tworzone w oparciu o plik z dniami pkl
# jeśli nie ma internetu/nie udało się pobrać danych i nie ma pliku: "nok" - nie powstają zmienne - wyrzucic blad i nie pobierac zmiennych!

#odswiezenie pogody, zwraca to samo co wyzej
#pogoda.get_weather()


#example of usage
print(pogoda.status)
print(pogoda.day[0].date)
print(pogoda.day[0].download_date)
print(pogoda.day[0].temperature_avg)
#pelna lista parametrow na dole pliku weather.py

