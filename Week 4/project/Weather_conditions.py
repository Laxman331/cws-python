import random

weather_conditions = ["Sunny", "Rainy", "Cloudy", "Snowy"]
number_of_days = int(input("Enter number of days for weather forecast = "))
for i in range(1, number_of_days + 1):
    a = random.randint(0, len(weather_conditions) - 1)
    print(f"Day{i}: {weather_conditions[a]}")
