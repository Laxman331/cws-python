"""Q1. Write a Python program to check if a string has at least one
letter and one number. If it has at least one letter and one number
then print YES else print NO."""

a = input("Enter a string =")
letter = False
number = False
for i in a:
    if i.isalpha():
        letter = True
    elif i.isdigit():
        number = True
if letter and number:
    print("Both number and letter exists")
else:
    print("Both number and letter does not exists")
