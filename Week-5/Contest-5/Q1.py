"""Q1. Count number of alphabets in a string entered by user.
Example input: abcd1234 xyz
Output: 7"""

a = input("Enter a string =")
b = list(a)
count = 0
for i in b:
    if i.isalpha():
        count = count + 1
print(count)
