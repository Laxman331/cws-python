""""Q3. Ask a string from user. Print the characters in a list whose
count is an ODD number.
Example input: aeroplane is a transport
Example output: ['r', 'l', ' ', 'i']
Example input: we are learning python
Example output: ['w', 'e', ' ', 'l', 'n', 'i', 'g', 'p', 'y', 't', 'h', 'o']
Example input: good
Example output: ['g','d']"""

a = input("enter a string =")
b = list(a)
c = []
for i in b:
    b.count(i)
    if b.count(i) % 2 != 0:
        c.append(i)
d = []
for i in c:
    if i not in d:
        d.append(i)
print(d)
