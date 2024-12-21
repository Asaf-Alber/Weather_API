import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

def plot_weather_data(forecast_data, city_name):
    times = [item['dt_txt'] for item in forecast_data['list']]
    temperatures = [item['main']['temp'] for item in forecast_data['list']]

    times = [datetime.strptime(time, '%Y-%m-%d %H:%M:%S') for time in times]

    print(f"Plotting weather data for {city_name}")
    print(f"Times: {times}")
    print(f"Temperatures: {temperatures}")

    plt.figure(figsize=(10, 6))
    plt.plot(times, temperatures, label='Temperature (°C)', color='tab:blue')

    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d/%m/%y %H:%M'))
    plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=3))
    plt.xticks(rotation=45, ha='right', fontsize=10)

    plt.xlabel('Date & Time')
    plt.ylabel('Temperature (°C)')
    plt.title(f'5-Day Forecast for {city_name}')
    plt.grid(True)
    plt.tight_layout()

    plt.show()
