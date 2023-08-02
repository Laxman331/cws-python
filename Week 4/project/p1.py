# a = ["c", "x", "y", "z"]
# c = random.randint(0, 3)
# print(c)
# print(a[c])

# import random
# weather_conditions = ["Sunny", "Rainy", "Cloudy", "Snowy"]
# number_of_days = int(input("Enter number of days for weather forecast = "))
# for Day in range(1, number_of_days + 1):
#     a = random.choice((weather_conditions))
#     print(f"Day{Day}: {a}")
a = [[1, 2], [10, 10, 10], [4, 5]]
sum = 0
for i in a:
    for j in i:
        sum = sum + j
print(sum)
