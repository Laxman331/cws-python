"""Q2. Write a function called dictionary_value_sum(d) that takes a
dictionary d as a parameter, where the values are numbers, and
returns the sum of all the values in the dictionary."""


def dictionary_value_sum(a: dict):
    sum = 0
    for v in a.values():
        sum = sum + v
    return sum


x = dictionary_value_sum({"a": 12, "b": 3, "c": 4, "d": 6})
print(x)
