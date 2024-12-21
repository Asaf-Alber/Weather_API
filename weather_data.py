import os
import time
from os import makedirs
import json
from os.path import exists

import requests

from config import config

def sanitize_filename(city):
    return city.replace(" ", "_").replace(",", "").replace(":", "").replace(".", "").replace("-", "_")

def save_weather_data_to_cache(city, weather_data):
    if not exists(config.CACHE_DIR):
        makedirs(config.CACHE_DIR)

    city_sanitized = sanitize_filename(city)
    cache_file_path = os.path.join(config.CACHE_DIR, f"{city_sanitized}_weather_cache.json")
    cached_data = {
        "weather_data": weather_data,
        "timestamp": time.time()
    }
    with open(cache_file_path, "w", encoding="utf-8") as f:
        json.dump(cached_data, f, indent=4)

def get_cached_weather(city):
    sanitized_city = sanitize_filename(city)
    cache_file_path = os.path.join(config.CACHE_DIR, f"{sanitized_city}_weather_cache.json")
    try:
        with open(cache_file_path, "r") as f:
            cached_data = json.load(f)
            if time.time() - cached_data["timestamp"] < config.CACHE_TIMEOUT:
                return cached_data["weather_data"]
            else:
                return None
    except FileNotFoundError:
        return None

def fetch_weather_data(params):
    try:
        response = requests.get(config.BASE_URL, params=params, timeout=10)
        response.raise_for_status()

        weather_data = response.json()
        if "main" in weather_data:
            return weather_data
        else:
            print("Unexpected response from weather API")
            return None
    except requests.RequestException as e:
        print(f"Failed to fetch weather data: {e}")
        return None

def get_weather(city, lang='en'):
    params = {"q": city, "appid": config.API_KEY, "units": "metric", "lang": lang}
    cached_data = get_cached_weather(city)
    if cached_data:
        print(f"Using cached data for {city}")
        return cached_data
    weather_data = fetch_weather_data(params)
    if weather_data:
        save_weather_data_to_cache(city, weather_data)
    return weather_data

def get_forecast(city, lang='en'):
    params = {"q": city, "appid": config.API_KEY, "units": "metric", "lang": lang}
    try:
        response = requests.get(config.FORECAST_URL, params=params, timeout=10)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Failed to fetch forecast data: {e}")
        return None


