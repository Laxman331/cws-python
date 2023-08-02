"""Q4. Read a file using python program. Print all the words in a
reverse order.
Example:
abc.txt
Hello Good morning
I am the best

Output
olleH dog gninorm
I ma eht tseb"""
f = open("xyz.txt", "r")
a = f.readlines()
b = []
for i in a:
    p = i.strip()
    b.append(p)
for i in b:
    print(i[::-1])
