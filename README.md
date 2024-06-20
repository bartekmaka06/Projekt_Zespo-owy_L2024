# Weather App

Required:
 - python-dateutil
 - requests
 - Pillow
 - io
 - tkinter
 - pickle

`weather.py`

This file contains the core functionality for fetching and processing weather data.

Classes:

- Weather
    - Attributes:
        - city: The city for which weather data is being fetched.
        - day: A list to store weather data for each day.
        - status: The status of the weather data retrieval process.
    - Methods:
        - __init__(self, city): Initializes the Weather object with the specified city and retrieves weather data.
        - get_weather(self): Clears existing data and attempts to download new weather data. If successful, stores data locally. Otherwise, retrieves data from a local file.
        - download_weather(self): Downloads weather data from the OpenWeatherMap API. Parses the data and populates the day list with Day objects.

- Day
    - Attributes:
        - date: The date for which weather data is applicable.
        - download_date: The timestamp when the weather data was downloaded.
        - temperature_avg: Average temperature for the day.
        - temperature_min: Minimum temperature for the day.
        - temperature_max: Maximum temperature for the day.
        - overall_icon: Icon representing the overall weather condition.
        - pressure: Atmospheric pressure.
        - humidity: Humidity percentage.
        - clouds: Cloud coverage percentage.
        - description: Weather description.
        - sunrise_utc: Sunrise time in UTC.
        - sunset_utc: Sunset time in UTC.
        - wind_speed: Wind speed.
        - sunrise: Local sunrise time.
        - sunset: Local sunset time.

`main.py`

This file contains the graphical user interface (GUI) for the weather app, built using the Tkinter library.

Functions:
- center_window(window, width, height): Centers the application window on the screen.
- get_and_resize_image(icon_id, width, height): Fetches and resizes weather icon images from OpenWeatherMap.
- create_button_callback(button_nr): Creates a callback function for day selection buttons.
- click_day_button(nr): Updates the GUI with weather data for the selected day.
- click_search_button(): Fetches and updates weather data for the city entered by the user.
- update_gui_with_weather_data(pogoda): Updates the GUI elements with the latest weather data.
- update_weather_images(pogoda): Updates the weather icons in the GUI.

Global Variables:
- pogoda: A global variable to store the Weather object.
- url_icon: The URL template for fetching weather icons.

GUI Elements:
- Main Window: Created using Tkinter's Tk class.
- Frames: Used to organize different sections of the GUI, such as search input, forecast display, and detailed weather information.
- Labels: Display text information like city name, temperature, weather description, etc.
- Buttons: Allow the user to search for a city's weather or select different days to view their weather details.
- Images: Display weather icons fetched and resized from the OpenWeatherMap API.

Workflow:
- Initialization:
    - The main window is created and centered.
    - Initial weather data for a default city ("Łódź") is fetched and displayed.
- Search:
    - The user can enter a city name and click the search button to fetch and display weather data for the new city.
- Day Selection:
    - The user can click on different day buttons to view detailed weather information for the selected day.
