from email_notifications import send_email_notification
from visualization import plot_weather_data
from weather_data import get_forecast, get_weather, get_weather_alerts

def main():
    city_name = input("Enter city name (default: 'London'): ")
    if not city_name:
        city_name = "London"
        print(f"No city entered. Defaulting to {city_name}.")

    lang = input("Enter preferred language (leave blank for 'en'): ") or 'en'
    weather_data = get_weather(city_name, lang)
    if not weather_data:
        print(f"Error: Could not retrieve weather data for '{city_name}'. Please try again.")
        return

    print(f"Weather for {city_name}:")
    print(f"Temperature: {weather_data['main']['temp']}°C")
    print(f"Humidity: {weather_data['main']['humidity']}%")
    print(f"Weather: {weather_data['weather'][0]['description'].capitalize()}")

    try:
        forecast_data = get_forecast(city_name, lang)
        if forecast_data:
            print("\n5-day forecast:")
            plot_weather_data(forecast_data, city_name)
            send_email_notification("Weather Update", f"Weather updates for {city_name}")
        else:
            print(f"Error: Could not retrieve weather data for {city_name}")
    except Exception as e:
        print(f"An error occurred while getting the forecast: {e}")            

if __name__ == "__main__":
    main()
