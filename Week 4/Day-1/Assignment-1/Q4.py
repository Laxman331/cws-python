"""Q4. Write a Python program to remove an item from a tuple."""
a = (3, 24, 15, 19, 10, 31, 22)
n = int(input("Enter element present in tuple = "))
b = list(a)
b.remove(n)
print(tuple(b))
