import random

weather_conditions = ["Sunny", "Rainy", "Cloudy", "Snowy"]
number_of_days = int(input("Enter number of days for weather forecast = "))
for Day in range(1, number_of_days + 1):
    a = random.choice((weather_conditions))
    print(f"Day{Day}: {a}")
