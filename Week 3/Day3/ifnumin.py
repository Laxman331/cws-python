a = [13, 14, 14, 18, 2, 8, 9]
num = int(input("Enter number = "))
b = a.count(num)
print(b)
if num in a:
    print("Same")
else:
    print("Not same")
