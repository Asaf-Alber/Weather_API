# 🌦️ Weather Data Automation Project

This Python-based project demonstrates a complete pipeline for interacting with a weather API. It showcases skills in modular programming, API integration, data visualization, and automated email notifications — all structured in a clean and scalable way.

---

## 🧠 What This Project Does

- 🔌 **Connects to a public Weather API** to fetch real-time weather data
- 📊 **Visualizes** temperature, humidity, and other parameters
- 📧 **Sends email notifications** if weather conditions meet defined thresholds
- 🧱 **Modular architecture** for clear separation of functionality

---

## 🛠️ Technologies & Skills Demonstrated

- **Python 3**
- **REST API** usage and error handling
- **Modular design principles** using separate `.py` files per feature
- **Data visualization** (e.g., matplotlib or seaborn)
- **Email automation** using SMTP
- **Secure configuration** management (`config.py` / `.env`)
- **Version control** with `.gitignore` and clean commits

---

## 📁 Project Structure

weather_api_project/
├── main.py # Entry point for running the project
├── config.py # Stores API keys and config variables
├── weather_data.py # Handles API calls and JSON parsing
├── visualization.py # Generates visual reports (charts, graphs)
├── email_notifications.py # Sends weather-based email alerts
├── .gitignore # Ensures sensitive files are not committed
└── README.md # Project documentation
