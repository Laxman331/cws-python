a = [55555, 3, 65, 45, 432, 5436, 756, 86789, 798, 798, 908, 123, 65, 45, 321, 4, 654]
start = int(input("Enter start index = "))
end = int(input("Enter end index = "))
for i in range(0, len(a)):
    if i == start:
        print(f" start index position is {a[i]}")
    elif i == end:
        print(f" end index position is {a[i]}")
for i in range(start, end + 1):
    print(a[i], end=" ")
