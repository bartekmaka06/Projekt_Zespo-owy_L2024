from weather import Weather
from tkinter import Tk, Label, Button, Frame, Entry, PhotoImage
from PIL import Image, ImageTk

def resized_image(image_path, width, height):
    original_image = Image.open(image_path)
    resized_image = original_image.resize((width, height), Image.LANCZOS)
    return resized_image

def create_button_callback(button_nr):
    return lambda: click_day_button(button_nr)

def click_day_button(nr):
    print("Selected: "+ str(nr))
    print("Day: ", label_day_l[nr-1].cget("text"))

def click_search_button():
    city = entry.get()
    print("Search: "+ city)
    #metoda config moze nam pomoc przy aktualizacji obiektow w trakcie dzialania aplikacji. Dzięki niej można edytować każdy atrybut widgetu
    #label_forecast.config(text="Weather forecast "+city)

root = Tk()
root.title('Weather App')
root.geometry("700x500")

frame_search = Frame(root)
entry = Entry(frame_search, width=30)
entry.pack(side="left")
click_button = Button(frame_search, text="Search", width=8, command=click_search_button)
click_button.pack(side="left")
frame_search.pack()

frame_forecast = Frame(root)
label_forecast = Label(frame_forecast, text="Weather forecast", font=30)
label_forecast.pack()
label_day = Label(frame_forecast, text="Monday", font=30)
label_day.pack()
frame_forecast.pack()

frame_center = Frame(root)

#info po lewej
frame_info_left = Frame(frame_center)
label_avg_temp_day = Label(frame_info_left, text="Day: 20*C", font=30)
label_avg_temp_day.pack()
label_avg_temp_night = Label(frame_info_left, text="Day: 3*C", font=30)
label_avg_temp_night.pack()
label_min_max_temp = Label(frame_info_left, text="Min: 1*C Max: 23*C", font=30)
label_min_max_temp.pack()
label_sunset = Label(frame_info_left, text="Sunset: 19:00", font=30)
label_sunset.pack()
label_sunrise = Label(frame_info_left, text="Sunrise: 5:00", font=30)
label_sunrise.pack()
frame_info_left.pack(side="left")

# obraz pogody
image_weather = ImageTk.PhotoImage(resized_image("sun_cloud.png",200,200), width=200, height=200)
label_photo = Label(frame_center, image=image_weather)
label_photo.pack(side="left")

#info po prawej
frame_info_right = Frame(frame_center)
label_pressure = Label(frame_info_right, text="Pressure: 1012 hPa", font=30)
label_pressure.pack()
label_rain = Label(frame_info_right, text="Rain: 0.0mm", font=30)
label_rain.pack()
label_cloud = Label(frame_info_right, text="Cloudy: 10%", font=30)
label_cloud.pack()
label_wind = Label(frame_info_right, text="Wind: 7km/h", font=30)
label_wind.pack()
label_air_humidity = Label(frame_info_right, text="Air humidity: 70%", font=30)
label_air_humidity.pack()
frame_info_right.pack(side="left")

frame_center.pack()


label_weather_info = Label(root, text="Sunny", font=30)
label_weather_info.pack()

#dolny panel dni do wyboru
frame_center2 = Frame(root)

frame_day_l = []
label_day_l = []
image_day_l = []
label_photo_day_l = []
label_avg_temp_day_l = []
button_day_l = []

test_temp = ["1*C", "2*C", "3*C", "4*C", "5*C"]
test_days = ["Mond", "Tue", "Wen", "Thu","Fri"]


for i in range (1,6):
    frame_day = Frame(frame_center2)
    frame_day_l.append(frame_day)

    label_day = Label(frame_day, text=test_days[i-1], font=30)
    label_day.pack()
    label_day_l.append(label_day)

    image_day = ImageTk.PhotoImage(resized_image("sun_cloud.png",60,60), width=60, height=60)
    image_day_l.append(image_day)
    label_photo_day = Label(frame_day, image=image_day)
    label_photo_day.pack()
    label_photo_day_l.append(label_photo_day)

    label_avg_temp_day = Label(frame_day, text=test_temp[i-1], font=30)
    label_avg_temp_day.pack()
    label_avg_temp_day_l.append(label_avg_temp_day)

    button_day = Button(frame_day, text="Select", width=8, command=create_button_callback(i))
    button_day.pack()
    button_day_l.append(button_day)

    frame_day.pack(side="left")


frame_center2.pack()

root.mainloop()


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
print(pogoda.day[0].sunrise)
print(pogoda.day[0].sunset)
#pelna lista parametrow na dole pliku weather.py

