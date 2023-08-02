a = {}
a["name"] = input("Enter name = ")
a["age"] = input(("Enter age ="))
a["gender"] = input("Enter gender = ")
for i in range(0, 6):
    sub = input("enter sub name = ")
    marks = int(input("Enter marks = "))
    a[sub] = marks
print(a)
