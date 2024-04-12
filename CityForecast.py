class CityForecast:
    def __init__(self, city):
        self.city = city
        self.temperature = None
        self.condition = None
        self.humidity = None

    def parse_weather_data(self, data):
        self.temperature = data["temperature"]
        self.condition = data["condition"]
        self.humidity = data["humidity"]

    def detailed_forecast(self):
        return f"{self.city} - {self.temperature} degrees, {self.condition}, {self.humidity}% humidity"
    
    def basic_forecast(self):
        return f"{self.city} - {self.temperature} degrees, {self.condition}"
