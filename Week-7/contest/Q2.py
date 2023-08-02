"""Q2. Write a Python program that takes a user's input for a file
name and a positive integer (n). The program should read the
content of the file and print the first n lines."""

file_name = input("Enter file name =")
n = int(input("Enter a positive number ="))
f = open(mode="r", file=file_name)
a = f.readlines()
b = []
for i in a:
    c = i.strip()
    b.append(c)
print(b)
for i in range(0, len(b)):
    if i == n:
        break
    else:
        print(b[i])
