"""Q5. Write a python program to split a string on vowels. Ask string
from user.
Example input: aeroplane
Example output: [r, pl, n]
Example input: We are LEArning Python
Example output: [W,  , r,  L, rn, ng, Pyth, n]
 """


a = input("Enter a string =")
b = a.split(" ")
c = []
print(b)
for i in b:
    for j in i:
        if j not in "aeiou":
            c.append(j)
print(c)
