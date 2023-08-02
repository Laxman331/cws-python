"""Q3. Write a python program to remove all the duplicates from the
string entered by user."""

a = input("Enter a string = ")
b = a.split()
c = []
for i in b:
    if i not in c:
        c.append(i)
print((c))
