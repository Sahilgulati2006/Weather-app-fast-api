import requests
from fastapi import HTTPException
import os

API_KEY = os.getenv("OPENWEATHER_API_KEY")
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_for_location(location: str):
    if not API_KEY:
        raise HTTPException(status_code=500, detail="OpenWeather API key not set.")

    params = {
        "q": location,
        "appid": API_KEY,
        "units": "metric"
    }
    response = requests.get(BASE_URL, params=params)

    if response.status_code != 200:
        print("DEBUG ERROR:", response.text)  # Log   API errors
        raise HTTPException(status_code=404, detail="Location not found or API error.")

    data = response.json()
    temperature = data["main"]["temp"]
    description = data["weather"][0]["description"]

    return temperature, description
