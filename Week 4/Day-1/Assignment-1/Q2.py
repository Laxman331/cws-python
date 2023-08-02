"""Q2. Write a Python program to find repeated items in a tuple."""
a = (3, 22, 61, 29, 22, 99, 48, 3, 29, 99, 6147, 22)
b = []
for i in a:
    a.count(i)
    if a.count(i) >= 2:
        b.append(i)
print(tuple(set(b)))
