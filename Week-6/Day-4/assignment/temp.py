a = [10, 20, 30]
b = [11, 10, 12, 43, 30]
c = []
for i in a:
    if i in b:
        c.append(i)

print(c)
