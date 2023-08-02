#     if i not in c:
#         c.append(i)
a = {"d": 1, "b": 2, "a": 3, "c": 1}
b = list(a.values())
print(max(b))
for k, v in a.items():
    if v == max(b):
        print(k)
