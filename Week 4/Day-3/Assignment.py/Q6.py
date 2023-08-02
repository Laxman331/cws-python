"""Q5. Write a Python program to remove duplicates from Dictionary.
Sample dictionary: dictionary = {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10,
1:60, 2:30,}"""

# a = {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10, 1: 80, 2: 90, 7: 60, 8: 50}
# b = []
# c = {}
# for k, v in a.items():
#     if k not in b:
#         b.append(k)
#         c[k] = v
# print(c)
a = {1: 60, 2: 50, 3: 40, 4: 30, 5: 20, 6: 10, 7: 60, 8: 50}
b = {}
c = {}
for k, v in a.items():
    if v not in b:
        b.update(v)
        c[k] = v
print(c)
