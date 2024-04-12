import random

class WeatherGenerator:
    def __init__(self):
        self.weather_descriptions = {
            "snowy": range(-10, 32),  # Snowy for temperatures from -10°F to 31°F
            "rainy": range(32, 61),   # Rainy for temperatures from 32°F to 60°F
            "cloudy": range(32, 101), # Cloudy can occur from 32°F to 100°F, overlapping with rain
            "sunny": range(50, 101)   # Sunny for temperatures from 50°F to 100°F
        }
    
    def create_random_forecast(self, city):
        temperature = random.randint(-10, 100)  # Expanded range for temperature
        possible_conditions = [condition for condition, temp_range in self.weather_descriptions.items() if temperature in temp_range]
        condition = random.choice(possible_conditions)  # Choose a condition based on the temperature
        humidity = random.randint(20, 100) if condition in ["rainy", "snowy"] else random.randint(10, 50)  # Higher humidity for rainy and snowy conditions
        return {
            "city": city,
            "temperature": temperature,
            "condition": condition,
            "humidity": humidity
        }
