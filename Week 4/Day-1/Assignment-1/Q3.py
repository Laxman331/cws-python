"""Q3. Write a Python program to check whether an element exists
within a tuple."""
a = (1, 23, 76, 43, 87, 71)
n = int(input("Enter number = "))
for i in a:
    if n == i:
        print("exists")
        break
if n != i:
    print("not exists")
