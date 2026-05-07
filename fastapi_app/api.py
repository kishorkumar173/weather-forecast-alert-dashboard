from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Get API key from .env
API_KEY = os.getenv("API_KEY")

# Create FastAPI app
app = FastAPI(
    title="Weather Forecast API",
    description="Professional Weather Dashboard Backend",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Home Route
@app.get("/")
def home():

    return {
        "message": "Weather API Running Successfully"
    }

@app.get("/weather/{location}")
def get_weather(location: str):

    try:

        # Clean location input
        formatted_location = location.strip()

        # WeatherAPI Forecast URL
        url = (
            f"http://api.weatherapi.com/v1/forecast.json"
            f"?key={API_KEY}"
            f"&q={formatted_location}"
            f"&days=7"
            f"&aqi=yes"
        )

        # Send request
        response = requests.get(url)

        # Convert response to JSON
        data = response.json()

        # Handle invalid locations
        if "error" in data:

            return {
                "success": False,
                "error": (
                    "Location not found. "
                    "Try full location name like "
                    "'Anekal Karnataka India'"
                )
            }

        # Weather Data
        weather_data = {

            "success": True,

            "city": data["location"]["name"],

            "region": data["location"]["region"],

            "country": data["location"]["country"],

            "local_time": data["location"]["localtime"],

            "temperature": data["current"]["temp_c"],

            "feels_like": data["current"]["feelslike_c"],

            "humidity": data["current"]["humidity"],

            "condition": data["current"]["condition"]["text"],

            "icon": "https:" + data["current"]["condition"]["icon"],

            "wind_speed": data["current"]["wind_kph"],

            "uv_index": data["current"]["uv"],

            "visibility": data["current"]["vis_km"],

            "aqi": data["current"]["air_quality"]["pm2_5"]
        }

        # Alerts
        alerts = []

        if weather_data["temperature"] > 35:
            alerts.append("🔥 Heat Alert")

        if weather_data["humidity"] > 80:
            alerts.append("💧 High Humidity Alert")

        if "rain" in weather_data["condition"].lower():
            alerts.append("🌧 Rain Alert")

        if weather_data["wind_speed"] > 40:
            alerts.append("🌪 Strong Wind Alert")

        # AQI Alert
        if weather_data["aqi"] > 50:
            alerts.append("😷 Poor Air Quality Alert")

        weather_data["alerts"] = alerts

        # Forecast Data
        forecast = []

        for day in data["forecast"]["forecastday"]:

            forecast.append({

                "date": day["date"],

                "max_temp": day["day"]["maxtemp_c"],

                "min_temp": day["day"]["mintemp_c"],

                "condition": day["day"]["condition"]["text"],

                "icon": "https:" + day["day"]["condition"]["icon"]
            })

        weather_data["forecast"] = forecast

        return weather_data

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

        # Current Weather
        weather_data = {

            "success": True,

            "city": data["location"]["name"],

            "region": data["location"]["region"],

            "country": data["location"]["country"],

            "local_time": data["location"]["localtime"],

            "temperature": data["current"]["temp_c"],

            "feels_like": data["current"]["feelslike_c"],

            "humidity": data["current"]["humidity"],

            "condition": data["current"]["condition"]["text"],

            "icon": "https:" + data["current"]["condition"]["icon"],

            "wind_speed": data["current"]["wind_kph"],

            "uv_index": data["current"]["uv"],

            "visibility": data["current"]["vis_km"]
        }

        # Alerts
        alerts = []

        if weather_data["temperature"] > 35:
            alerts.append("🔥 Heat Alert")

        if weather_data["humidity"] > 80:
            alerts.append("💧 High Humidity Alert")

        if "rain" in weather_data["condition"].lower():
            alerts.append("🌧 Rain Alert")

        weather_data["alerts"] = alerts

        # Forecast Data
        forecast = []

        for day in data["forecast"]["forecastday"]:

            forecast.append({

                "date": day["date"],

                "max_temp": day["day"]["maxtemp_c"],

                "min_temp": day["day"]["mintemp_c"],

                "condition": day["day"]["condition"]["text"],

                "icon": "https:" + day["day"]["condition"]["icon"]
            })

        weather_data["forecast"] = forecast

        return weather_data

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }

        # WeatherAPI URL
        url = (
            f"http://api.weatherapi.com/v1/current.json"
            f"?key={API_KEY}&q={location}"
        )

        # Send request
        response = requests.get(url)

        # Convert response to JSON
        data = response.json()

        # Handle invalid locations
        if "error" in data:

            return {
                "success": False,
                "error": data["error"]["message"]
            }

        # Extract weather data
        weather_data = {

            "success": True,

            "city": data["location"]["name"],

            "region": data["location"]["region"],

            "country": data["location"]["country"],

            "local_time": data["location"]["localtime"],

            "temperature": data["current"]["temp_c"],

            "feels_like": data["current"]["feelslike_c"],

            "humidity": data["current"]["humidity"],

            "condition": data["current"]["condition"]["text"],

            "icon": "https:" + data["current"]["condition"]["icon"],

            "wind_speed": data["current"]["wind_kph"],

            "uv_index": data["current"]["uv"],

            "visibility": data["current"]["vis_km"]
        }

        # Weather Alerts
        alerts = []

        if weather_data["temperature"] > 35:
            alerts.append("🔥 Heat Alert")

        if weather_data["humidity"] > 80:
            alerts.append("💧 High Humidity Alert")

        if "rain" in weather_data["condition"].lower():
            alerts.append("🌧 Rain Alert")

        if weather_data["wind_speed"] > 40:
            alerts.append("🌪 Strong Wind Alert")

        # Add alerts
        weather_data["alerts"] = alerts

        return weather_data

    except Exception as e:

        return {
            "success": False,
            "error": str(e)
        }