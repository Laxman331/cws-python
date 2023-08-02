"""n = int(input("Enter the number = "))
count = 0
for i in range(1, n + 1):
    fact = 0
    for j in range(1, n + 1):
        if i % j == 0:
            fact = fact + 1
    if fact == 2:
        count = count + 1
print(count)"""
# =int(input("Enter number = "))
# if n%10 ==0:
#     printn
a = []
n1 = int(input("Enter number1 = "))
n2 = int(input("Enter number2 = "))
n3 = int(input("Enter number3 = "))
n4 = int(input("Enter number4 = "))
n5 = int(input("Enter number5 = "))
n6 = int(input("Enter number6 = "))
n7 = int(input("Enter number7 = "))
n8 = int(input("Enter number8 = "))
n9 = int(input("Enter number9 = "))
n10 = int(input("Enter number10 = "))
a.append(n1)
a.append(n2)
a.append(n3)
a.append(n4)
a.append(n5)
a.append(n6)
a.append(n7)
a.append(n8)
a.append(n9)
a.append(n10)
b = a.copy()
b.reverse()
print(b)
