"""Q5. Given a list of integers, print all the prime numbers present in the list."""

a = [12, 5, 2, 4, 63, 13, 42, 17, 23, 99, 77, 11]
b = []
for i in a:
    div = 0
    for j in range(1, i + 1):
        if i % j == 0:
            div = div + 1
    if div <= 2:
        b.append(i)
print(b)
