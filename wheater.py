from typing import final
import requests
import json
import os

KEY = "api_key"
FILE = "wheater.json"

def loadCities():
    if os.path.isfile(FILE):
        with open(FILE, "r") as input:
            if os.stat(FILE).st_size != 0:
                return json.load(input)
    return dict()

def addCity(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={KEY}&units=metric"
    response = requests.get(url)
    
    if response.status_code == 200:
        final_data = loadCities()

        data = json.loads(response.text)
        out = {
            data["name"]: {
                "temp": data["main"]["temp"],
                "wind": data["wind"]["speed"],
                "humidity": data["main"]["humidity"]
            }
        }

        final_data.update(out)

        with open(FILE, "w") as output: 
            json.dump(final_data, output, indent=4)
