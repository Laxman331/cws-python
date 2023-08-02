a = [23, 32, 44, 23, 18, 44]
b = []
for i in a:
    if i not in b:
        b.append(i)
print(b)

for i in b:
    count = a.count(i)
    print(f"{i} occurs in {count} times")
