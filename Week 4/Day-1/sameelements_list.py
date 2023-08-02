a = [12, 87, 77, 34, 65, 98]
b = [12, 43, 98, 28, 76, 79]
c = set(a).union(set(b))
d = list(c)
print(d)
e = list(set(a).intersection(set(b)))
print(e)
