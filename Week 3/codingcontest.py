"""Q1. Given a list of numbers. Write a program to turn every item of a list into its square.
numbers = [1, 2, 3, 4, 5, 6, 7]
Expected output: [1, 4, 9, 16, 25, 36, 49]"""

a = [1, 2, 3, 4, 5, 6, 7]
b = []
for i in a:
    c = i * i
    b.append(c)
print(b)
