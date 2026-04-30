# CS 335 — Introduction to Artificial Intelligence
# API Assignment Starter Code — Northeastern Illinois University
#
# TODO: Replace BASE_URL, endpoints, params, and payload fields
#       with values from your chosen API's documentation.
# ─────────────────────────────────────────────────────────────

import os
import json
import requests
from dotenv import load_dotenv

load_dotenv()

# Open-Meteo is a free API for non-commercial use and does NOT require an API key.
# The code below bypasses the strict key check but shows where it would normally live.
API_KEY = os.getenv("MY_API_KEY", "not-needed")

# TODO: Replace with your API's base URL
BASE_URL = "https://api.open-meteo.com/v1/forecast"
# Base URL for Geocoding (used in call 2 & 3 to search for locations)
GEO_URL = "https://geocoding-api.open-meteo.com/v1/search"

# Open-Meteo doesn't require an Authorization header, so we just use Content-Type.
HEADERS = {
    "Content-Type": "application/json",
}

def divider(label):
    print(f"\n{'=' * 50}\n{label}\n{'=' * 50}")

# ── Call 1: GET request ───────────────────────────────────
# Use for retrieving weather data without a request body.
def call_one_get():
    divider("CALL 1 — GET Request (Current Weather in Berlin)")

    url = BASE_URL
    params = {
        "latitude": 52.52,
        "longitude": 13.41,
        "current": "temperature_2m,wind_speed_10m",
        "hourly": "temperature_2m",
        "past_days": 0,
        "forecast_days": 1
    }

    response = requests.get(url, headers=HEADERS, params=params)

    if response.status_code == 200:
        data = response.json()
        print(f"Current Temp: {data['current']['temperature_2m']}°C")
        print(f"Current Wind Speed: {data['current']['wind_speed_10m']} km/h")
    else:
        print(f"[ERROR] {response.status_code}: {response.text}")


# ── Call 2: POST request (Adapted to GET for Geocoding) ───
# Open-Meteo uses GET requests. This function is adapted to search for a city's coordinates.
def call_two_post():
    divider("CALL 2 — Geocoding Request (Adapted from POST)")

    url = GEO_URL
    # Finding the coordinates for Tokyo
    params = {
        "name": "Tokyo",
        "count": 1,
        "language": "en",
        "format": "json"
    }

    response = requests.get(url, headers=HEADERS, params=params)

    if response.status_code == 200:
        data = response.json()
        results = data.get("results", [])
        if results:
            city = results[0]
            print(f"Found {city['name']}, {city['country']} at Lat: {city['latitude']}, Lon: {city['longitude']}")
        else:
            print("Location not found.")
    else:
        print(f"[ERROR] {response.status_code}: {response.text}")


# ── Call 3: Parameterized POST  ────────────────────────────
# Accepts dynamic input (a city name), finds coordinates, and gets the weather.
def call_three_parameterized(user_input: str):
    divider(f"CALL 3 — Parameterized GET | input: '{user_input}'")

    # Step 1: Convert city name to coordinates
    geo_response = requests.get(GEO_URL, params={"name": user_input, "count": 1})
    
    if geo_response.status_code != 200 or not geo_response.json().get("results"):
        print(f"[ERROR] Could not resolve location: {user_input}")
        return

    location = geo_response.json()["results"][0]
    lat, lon = location["latitude"], location["longitude"]
    print(f"Resolved '{user_input}' -> {location['name']} ({lat}, {lon})")

    # Fetch the weather using the retrieved coordinates
    forecast_params = {
        "latitude": lat,
        "longitude": lon,
        "current": "temperature_2m,weather_code"
    }
    
    response = requests.get(BASE_URL, headers=HEADERS, params=forecast_params)

    if response.status_code == 200:
        data = response.json()
        temp = data.get("current", {}).get("temperature_2m", "N/A")
        print(f"Result: The current temperature in {location['name']} is {temp}°C")
    else:
        print(f"[ERROR] {response.status_code}: {response.text}")


if __name__ == "__main__":
    call_one_get()
    call_two_post()
    call_three_parameterized("Chicago")