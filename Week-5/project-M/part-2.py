a = {"og": {"d": "s", "ry": 21, "ge": "gg"}, "don": {"d": "r", "ry": 11, "ge": "cc"}}
movie = input("enter movie =")
x = str(input("Enter which details of the movie to be updated ="))
y = input("Enter your final updated detail =")
for k, v in a.items():
    if k == movie:
        v[(str(x))] = y
print(a)
