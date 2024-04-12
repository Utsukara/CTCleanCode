from CityForecast import CityForecast
from WeatherGenerator import WeatherGenerator

def ui():
    weather_generator = WeatherGenerator()
    while True:
        print("1. What city would you like to see the weather for?")
        print("2. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            city = input("Enter city: ")
            detailed = input("Detailed forecast? (y/n): ")
            data = weather_generator.create_random_forecast(city)
            forecast = CityForecast(city)
            forecast.parse_weather_data(data)
            if detailed.lower() == "y":
                print(forecast.detailed_forecast())
            else:
                print(forecast.basic_forecast())
        elif choice == "2":
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    ui()
