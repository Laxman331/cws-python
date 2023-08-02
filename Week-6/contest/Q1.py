"""Q1. Write a function called list_average(lst) that takes a list of
numbers lst as a parameter and returns the average of the
numbers in the list."""


def list_average(a: list):
    average = sum(a) / len(a)
    return average


c = [10, 30, 20, 40, 100, 60]
x = list_average(c)
print(x)
