"""Q1. Write a Python program to generate and print a dictionary that
contains a number (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
Ask n from user."""

a = {}
n = int(input("Enter number = "))
for i in range(1, n + 1):
    a[i] = i * i
print(a)
