"""Q3. Given a Python list, write a program to remove all occurrences of item 70.
list1 = [70, 20, 15, 70, 25, 50, 20]
Expected output: [20, 15, 25, 50, 20]"""

list1 = [70, 20, 15, 70, 25, 50, 20]
a = []
for i in range(0, len(list1)):
    if list1[i] == 70:
        continue
    else:
        a.append(list1[i])
print(a)
