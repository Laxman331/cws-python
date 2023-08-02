a = {12, 3, 2, 98, 45, 32, 98}
b = {12, 4, 98, 87, 62}
c = a.union(b)
d = a.intersection(b)
e = list(a)
e[0] = 100
e.pop(2)
e.append(99)
print(e)
