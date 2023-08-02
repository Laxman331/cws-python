"""Q1. Write a Python program to check if a string is empty or not."""
a = input("Enter a string =")
b = list(a)
count = 0
for i in b:
    c = b.count(i)
    if c > count:
        count = c
if count >= 1:
    print("string is not empty")
else:
    print("string is empty")
