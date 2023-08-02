"""Q1. Make your own dictionary. Write a Python code where the keys
and values are inverted. The values in the original dictionary
should be unique, ensuring that the inverted dictionary is valid.
Sample input: {"a": 1,"b": 2, "c": 3}
Output: {1: "a", 2: "b", 3: "c"}"""

a = {"a": 1, "b": 2, "c": 3}
b = {}
for k, v in a.items():
    b[v] = k
print(b)
