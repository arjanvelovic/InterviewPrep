import requests
import os
import platform

current_platform = platform.system()

if current_platform == 'Windows':
    platform_clear = 'cls'
else:
    platform_clear = 'clear'

os.system(platform_clear)

def get_weather(lat, lon):
    main_response = requests.get(f"https://api.weather.gov/points/{lat},{lon}")
    
    if main_response.status_code == 200:
        all_weather_data = main_response.json()

        city = all_weather_data['properties']['relativeLocation']['properties']['city']
        state = all_weather_data['properties']['relativeLocation']['properties']['state']

        print(f'Location: {city}, {state}')


        forecast_url = all_weather_data['properties']['forecast']

        if forecast_url == None:
            print('Uh-Oh something went wrong')
        else:
            forecast_response = requests.get(forecast_url)

            if forecast_response.status_code == 200:
                forecast = forecast_response.json()
                current_forecast = forecast['properties']['periods'][0]

                current_temperature = current_forecast['temperature']
                current_temperature_unit = current_forecast['temperatureUnit']
                current_short_forecast = current_forecast['shortForecast']
                current_precipitation = current_forecast['probabilityOfPrecipitation']['value']
                if current_precipitation == None:
                    current_precipitation = 0
                current_wind_speed = current_forecast['windSpeed']
                current_wind_direction = current_forecast['windDirection']

                print(f"""Currect Forecast: {current_short_forecast}
Temperature: {current_temperature} {current_temperature_unit}
Precipitation: {current_precipitation} %
Wind: {current_wind_speed} {current_wind_direction}""")
            else:
                print('Uh-Oh something went wrong')

    else:
        print('Uh-Oh something went wrong')


print('This is a US weather app')
lat = 0
lon = 0
while lat < 30 or lat > 48:
    lat = int(input("Input your latitude in range 30,48:"))
while lon < -120 or lon > -70:
    lon = int(input("Input your longitude in range -120,-75:"))
print("----------------------------------------")
get_weather(lat, lon)