"""Q5. Write a python program. Only print those lines which contains
‘a’ in it."""
f = open("xyz.txt", "r")
a = f.readlines()
b = []
for i in a:
    p = i.strip()
    b.append(p)
print(b)
for i in b:
    for j in i:
        if "a" == j:
            print(i)
