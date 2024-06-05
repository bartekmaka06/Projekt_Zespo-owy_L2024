from weather import Weather
from tkinter import Tk, Label, Button, Frame, Entry, PhotoImage
from PIL import Image, ImageTk
from datetime import datetime
import requests
from io import BytesIO
from skimage import segmentation
import numpy as np

global pogoda  # Declare the variable as global to modify it within the function
url_icon = 'https://openweathermap.org/img/wn/'

def get_and_resize_image(icon_id, width, height):
    response = requests.get(url_icon + f'{icon_id}@2x.png')
    image_data = response.content
    original_image = Image.open(BytesIO(image_data))
    resized_image = original_image.resize((width, height), Image.LANCZOS)
    return resized_image

def create_button_callback(button_nr):
    return lambda: click_day_button(button_nr)

def click_day_button(nr):
    print("Selected: "+ str(nr))
    print("Day: ", label_day_l[nr-1].cget("text"))

def click_search_button():
    city = entry.get()
    print("Search: " + city)
    # Update the pogoda variable with new weather data for the specified city
    pogoda = Weather(city)

    # Update the labels and images in the GUI with the new weather data
    update_gui_with_weather_data(pogoda)

def update_gui_with_weather_data(pogoda):
    # Update the labels and images with the new weather data
    # For example:
    label_date.config(text="Last update: " + pogoda.day[0].download_date.strftime("%Y-%m-%d %H:%M:%S"))
    print("label_day: " + pogoda.day[0].download_date.strftime("%A"))
    label_day.config(text=pogoda.day[0].download_date.strftime("%A"))
    label_city.config(text=pogoda.city.capitalize())
    label_avg_temp_day.config(text="Avg temp: " + str(int(pogoda.day[0].temperature_avg)) + " °C")
    label_min_max_temp.config(text="Min: " + str(int(pogoda.day[0].temperature_min)) + " °C Max: " + str(int(pogoda.day[0].temperature_max)) + " °C")
    label_sunset.config(text="Sunset: " + pogoda.day[0].sunset)
    label_sunrise.config(text="Sunrise: " + pogoda.day[0].sunrise)
    label_weather_info.config(text=pogoda.day[0].description.capitalize())
    label_pressure.config(text="Pressure: " + str(pogoda.day[0].pressure) + " hPa")
    label_cloud.config(text="Cloudy: " + str(pogoda.day[0].clouds) + "%")
    label_wind.config(text="Wind: " + str(pogoda.day[0].wind_speed) + " m/s")
    label_air_humidity.config(text="Air humidity: " + str(pogoda.day[0].humidity) + "%")

    # Update the weather images
    update_weather_images(pogoda)

def update_weather_images(pogoda):
    # Update the main weather image
    image_weather = ImageTk.PhotoImage(get_and_resize_image(pogoda.day[0].overall_icon, 200, 200))
    label_photo.config(image=image_weather)
    label_photo.image = image_weather  # Keep a reference to prevent image from being garbage collected

    # Update the daily weather images
    for i in range(1, 6):
        image_day = ImageTk.PhotoImage(get_and_resize_image(pogoda.day[i].overall_icon, 60, 60))
        label_photo_day_l[i - 1].config(image=image_day)
        label_photo_day_l[i - 1].image = image_day  # Keep a reference to prevent image from being garbage collected
        label_day_l[i - 1].config(text=pogoda.day[i].download_date.strftime("%A"))
        label_avg_temp_day_l[i - 1].config(text=str(int(pogoda.day[i].temperature_avg)))

root = Tk()
root.title('Weather App')
root.geometry("700x550")

# Set the background color
bg_color = "#E0FFFF"  # Light blue

# Apply the background color to the root window
root.configure(bg=bg_color)

pogoda = Weather("Łódź")

frame_search = Frame(root, bg=bg_color)

current_date = pogoda.day[0].download_date
formatted_datetime_str = current_date.strftime("%Y-%m-%d %H:%M:%S")
text_date = "Last update: " + formatted_datetime_str
label_date = Label(frame_search, text=text_date, font=("Helvetica", 8), bg=bg_color)
label_date.pack()
entry = Entry(frame_search, width=25, font=("Helvetica", 12))
entry.pack(side="left")
click_button = Button(frame_search, text="Search", font=("Helvetica", 12), width=8, height=1, command=click_search_button, relief="groove")
click_button.pack(side="left", padx=3)
frame_search.pack()

frame_forecast = Frame(root, bg=bg_color)
label_city = Label(frame_forecast, text="Łódź", font=("Helvetica", 25), bg=bg_color)
label_city.pack()
label_day = Label(frame_forecast, text=current_date.strftime("%A"), font=("Helvetica", 18), bg=bg_color)
label_day.pack()
frame_forecast.pack()

frame_center = Frame(root, bg=bg_color)

#info po lewej
frame_info_left = Frame(frame_center, bg=bg_color, width=200)
label_avg_temp_day = Label(frame_info_left, text="Avg temp: " + str(int(pogoda.day[0].temperature_avg)) + " °C", font=30, bg=bg_color)
label_avg_temp_day.pack()
# label_avg_temp_night = Label(frame_info_left, text="Night: " + str(pogoda.temperature_min), font=30)
# label_avg_temp_night.pack()
label_min_max_temp = Label(frame_info_left, text="Min: " + str(int(pogoda.day[0].temperature_min)) + " °C Max: " + str(int(pogoda.day[0].temperature_max)) + " °C", font=30, bg=bg_color)
label_min_max_temp.pack()
label_sunrise = Label(frame_info_left, text="Sunrise: " + pogoda.day[0].sunrise, font=30, bg=bg_color)
label_sunrise.pack()
label_sunset = Label(frame_info_left, text="Sunset: " + pogoda.day[0].sunset, font=30, bg=bg_color)
label_sunset.pack()
frame_info_left.pack(side="left")

# obraz pogody
image_weather = ImageTk.PhotoImage(get_and_resize_image(pogoda.day[0].overall_icon,200,200), width=200, height=200)
label_photo = Label(frame_center, image=image_weather, bg=bg_color)
label_photo.pack(side="left")

#info po prawej
frame_info_right = Frame(frame_center, bg=bg_color, width=200)
label_pressure = Label(frame_info_right, text="Pressure: " + str(pogoda.day[0].pressure) + " hPa", font=30, bg=bg_color)
label_pressure.pack()
# label_rain = Label(frame_info_right, text="Rain: " + pogoda.rain, font=30)
# label_rain.pack()
label_cloud = Label(frame_info_right, text="Cloudy: " + str(pogoda.day[0].clouds) + "%", font=30, bg=bg_color)
label_cloud.pack()
label_wind = Label(frame_info_right, text="Wind: " + str(pogoda.day[0].wind_speed) + " m/s", font=30, bg=bg_color)
label_wind.pack()
label_air_humidity = Label(frame_info_right, text="Air humidity: " + str(pogoda.day[0].humidity) + "%", font=30, bg=bg_color)
label_air_humidity.pack()
frame_info_right.pack(side="left")

frame_center.pack()


label_weather_info = Label(root, text=pogoda.day[0].description.capitalize(), font=30, bg=bg_color)
label_weather_info.pack()
frame_space = Frame(root, height=20, bg=bg_color)  # Możesz dostosować wysokość według potrzeb
frame_space.pack()
#dolny panel dni do wyboru
frame_center2 = Frame(root, bg=bg_color)

frame_day_l = []
label_day_l = []
image_day_l = []
label_photo_day_l = []
label_avg_temp_day_l = []
button_day_l = []

for i in range (1,6):
    frame_day = Frame(frame_center2, bg=bg_color, bd=2, relief="groove")
    frame_day_l.append(frame_day)

    print("day name: " + pogoda.day[i].download_date.strftime("%A"))
    label_day = Label(frame_day, text=pogoda.day[i].download_date.strftime("%A"), font=30, bg=bg_color)
    label_day.pack()
    label_day_l.append(label_day)

    image_day = ImageTk.PhotoImage(get_and_resize_image(pogoda.day[i].overall_icon,60,60), width=60, height=60)
    image_day_l.append(image_day)
    label_photo_day = Label(frame_day, image=image_day, bg=bg_color)
    label_photo_day.pack()
    label_photo_day_l.append(label_photo_day)

    label_avg_temp_day = Label(frame_day, text=str(int(pogoda.day[i].temperature_avg)), font=30, bg=bg_color)
    label_avg_temp_day.pack()
    label_avg_temp_day_l.append(label_avg_temp_day)

    button_day = Button(frame_day, text="Select", width=12, command=create_button_callback(i))
    button_day.pack()
    button_day_l.append(button_day)

    frame_day.pack(side="left", padx=3)


frame_center2.pack()

root.mainloop()


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
