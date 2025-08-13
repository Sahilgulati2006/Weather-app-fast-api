import requests
from typing import Tuple

# Replace with your actual API key
API_KEY = "YOUR_OPENWEATHERMAP_API_KEY"
BASE_URL = "https://api.openweathermap.org/data/2.5/weather"

def get_weather_for_location(latitude: float, longitude: float) -> Tuple[float, str]:
    """
    Fetch live weather data for a given latitude and longitude.
    Returns: (temperature in Celsius, weather description)
    """
    params = {
        "lat": latitude,
        "lon": longitude,
        "appid": API_KEY,
        "units": "metric"  # Celsius
    }

    try:
        response = requests.get(BASE_URL, params=params)
        response.raise_for_status()
        data = response.json()

        temp = data["main"]["temp"]
        description = data["weather"][0]["description"]
        return temp, description

    except requests.exceptions.RequestException as e:
        raise RuntimeError(f"Error fetching weather data: {e}")
    except (KeyError, IndexError):
        raise RuntimeError("Unexpected response format from weather API")
