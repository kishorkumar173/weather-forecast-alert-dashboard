import requests
from dotenv import load_dotenv
import os
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

# Load environment variables
load_dotenv()

# API Key
API_KEY = os.getenv("API_KEY")

# User input
city = input("Enter city name: ")

# API URL
url = f"http://api.weatherapi.com/v1/current.json?key={API_KEY}&q={city}"

# Request data
response = requests.get(url)

# Convert JSON
data = response.json()

# Extract data
temperature = data["current"]["temp_c"]
humidity = data["current"]["humidity"]
condition = data["current"]["condition"]["text"]
wind_speed = data["current"]["wind_kph"]

# Display weather
print("\n===== CURRENT WEATHER =====")

print(f"City: {city}")
print(f"Temperature: {temperature} °C")
print(f"Humidity: {humidity}%")
print(f"Condition: {condition}")
print(f"Wind Speed: {wind_speed} kph")

# Alerts
alerts = []

if temperature > 35:
    alerts.append("🔥 Heat Alert!")

if humidity > 80:
    alerts.append("💧 High Humidity Alert!")

if "rain" in condition.lower():
    alerts.append("🌧 Rain Alert!")

print("\n===== ALERTS =====")

if alerts:
    for alert in alerts:
        print(alert)
else:
    print("No alerts")

# Create DataFrame
weather_report = pd.DataFrame({
    "City": [city],
    "Temperature": [temperature],
    "Humidity": [humidity],
    "Condition": [condition],
    "Wind Speed": [wind_speed],
    "Date": [datetime.now()]
})

# Save CSV report
report_path = f"reports/{city}_weather_report.csv"

weather_report.to_csv(report_path, index=False)

print(f"\nReport saved: {report_path}")

# Visualization
labels = ["Temperature", "Humidity", "Wind Speed"]
values = [temperature, humidity, wind_speed]

plt.figure(figsize=(6,4))
plt.bar(labels, values)

plt.title(f"Weather Data for {city}")

chart_path = f"outputs/{city}_weather_chart.png"

plt.savefig(chart_path)

print(f"Chart saved: {chart_path}")

plt.show()