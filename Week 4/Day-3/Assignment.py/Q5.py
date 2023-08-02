"""Q5. Write a Python program to remove duplicates from Dictionary.
Sample dictionary: dictionary = {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10,
7:60, 8:50}
Output: {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10}"""

a = {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10, 7: 60, 8: 50}
b = []
c = {}
for k, v in a.items():
    if v not in b:
        b.append(v)
        c[k] = v
print(c)
