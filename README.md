Weather Forecast & Alert Application 🌦️

A full-stack Weather Forecast & Alert Application built using Next.js, FastAPI, and WeatherAPI that provides real-time weather updates, 7-day forecasts, weather alerts, analytics charts, and GPS-based location detection.

🚀 Live Demo
Frontend (Vercel)
PASTE_YOUR_VERCEL_LINK_HERE
Backend API (Render)
PASTE_YOUR_RENDER_LINK_HERE
📌 Project Overview

This project is a real-time weather intelligence platform designed to provide accurate weather forecasts, environmental insights, and weather alerts for different locations.

The application fetches live weather data using public APIs, analyzes conditions such as temperature, humidity, wind speed, and air quality, and displays them through an interactive dashboard.

The system also includes:

7-day weather forecasting
GPS-based current location weather
Weather analytics charts
Weather alert system
Responsive modern UI


🎯 Problem Statement

People often need accurate and quick weather information for:

travel planning
agriculture
logistics
event management
outdoor activities
public safety

Traditional weather systems can be complex and difficult to access programmatically.

This project solves the problem by creating a simple, responsive, and real-time weather dashboard with forecasting and alert capabilities.

✨ Features
🌍 Real-Time Weather Data
📅 7-Day Weather Forecast
📍 GPS-Based Current Location Weather
🌡 Temperature Analytics
🚨 Weather Alert System
💧 Humidity Monitoring
🌬 Wind Speed Tracking
☀ UV Index Monitoring
👁 Visibility Tracking
📊 Interactive Charts using Recharts
📱 Fully Responsive UI
⚡ FastAPI Backend API
🎨 Modern Next.js Frontend



🛠 Tech Stack
Frontend
Next.js
React.js
Tailwind CSS
Recharts
Backend
FastAPI
Python
Requests
WeatherAPI



Deployment
Vercel (Frontend)
Render (Backend)
📂 Project Structure

Weather-Forecast-Alert-Application/

├── fastapi_app/
│   ├── api.py
│
├── weather-dashboard/
│   ├── app/
│   ├── public/
│   ├── package.json
│
├── images/
├── outputs/
├── reports/
├── README.md
├── requirements.txt
└── .env.example


Installation & Setup
1️⃣ Clone Repository
git clone YOUR_GITHUB_REPOSITORY_LINK

2️⃣ Backend Setup
Create Virtual Environment
python -m venv venv
Activate Virtual Environment
Windows
venv\\Scripts\\activate
Mac/Linux
source venv/bin/activate
Install Backend Dependencies
pip install -r requirements.txt
3️⃣ Frontend Setup

Go to frontend folder:

cd weather-dashboard

Install dependencies:

npm install
🔑 Environment Variables

Create .env file:

API_KEY=your_weatherapi_key

Get API key from:

WeatherAPI

▶️ Run Backend
uvicorn fastapi_app.api:app --reload

Backend runs on:

http://127.0.0.1:8000
▶️ Run Frontend
npm run dev

Frontend runs on:

http://localhost:3000
📊 API Endpoints
Home Route
/
Weather Route
/weather/{location}

Example:

/weather/Bangalore
📈 Weather Analytics

The application visualizes:

maximum temperature trends
minimum temperature trends
weather conditions
humidity analysis
environmental insights

using interactive charts.

🚨 Alert System

The application generates alerts for:

High Temperature
High Humidity
Rain Conditions
Strong Wind Conditions
Poor Air Quality
🌍 GPS Location Support

Users can fetch weather using:

city names
district names
current GPS location
📱 Responsive Design

The dashboard is fully responsive and works on:

desktop
tablet
mobile devices

📸 Screenshots

Add screenshots in:

images/

Suggested screenshots:

Homepage
Weather Results
Forecast Cards
Charts
Alerts
Mobile View

🧠 Learning Outcomes

Through this project, I learned:

Full-Stack Development
API Integration
FastAPI Backend Development
Next.js Frontend Development
Weather Data Processing
Data Visualization
Deployment using Vercel & Render
Responsive UI Design
Error Handling
Production Deployment Workflow

💼 Industry Relevance
This project demonstrates skills relevant for:

Python Developer Roles
Full Stack Developer Roles
API Integration Projects
Frontend Development
Backend Engineering
Data Visualization Systems
Weather Analytics Platforms

🔮 Future Improvements
User Authentication
Weather History Database
AI-Based Weather Prediction
Multi-Language Support
Advanced Geolocation Search
Push Notifications
Dark/Light Theme Toggle


👨‍💻 Author
Kishor Kumar L

Built with ❤️ using Python, FastAPI, Next.js, and WeatherAPI.