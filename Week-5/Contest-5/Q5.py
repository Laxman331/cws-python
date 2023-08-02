"""Q5. Write a python program to split a string on vowels. Ask string
from user.
 """

a = input("Enter a string =")
b = a.split(" ")
print(b)
c = []
if len(b) == 1:
    for i in list(a):
        if i not in "aeiou":
            c.append(i)
elif len(b) >= 2:
    for i in list(a):
        if i not in "aeiou":
            c.append(i)
print(c)
