a = [41, 74, 23, 86, 42]
odd = []
even = []
for i in range(0, len(a)):
    if a[i] % 2 != 0:
        odd.append(a[i])
    else:
        even.append(a[i])
print(odd)
print(even)
