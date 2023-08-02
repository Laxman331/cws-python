"""Q2. Write your own dictionary. Write a python code to sort the
dictionary by values.
a = {"a": 5, "b": 2, "c": 10,"d":1}"""

a = {"a": 5, "b": 2, "c": 10, "d": 1}
b = sorted(a.values())
c = {}
for i in b:
    for k, v in a.items():
        if i == v:
            c.update({k: v})
print(c)
