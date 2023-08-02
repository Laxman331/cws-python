# n0 = int(input("Enter  Number1 = "))
# n1 = int(input("Enter  Number2 = "))
# n2 = int(input("Enter  Number3 = "))
# n3 = int(input("Enter  Number4 = "))
# n4 = int(input("Enter  Number5 = "))
# n5 = int(input("Enter  Number6 = "))
# n6 = int(input("Enter  Number7 = "))
# n7 = int(input("Enter  Number8 = "))
# n8 = int(input("Enter  Number9 = "))
# n9 = int(input("Enter  Number10 = "))
# b = []
# # for i in range(0, 10):
# b.extend([n0, n1, n2, n3, n4, n5, n6, n7, n8, n9])
# print([b])
# a = [18, 21, 13, 34, 65, 26, 57, 38, 49, 10]
# a.sort()
# print(f"Second Largest number is {a[-2]}")
# a = [18, 21, 13, 34, 13, 65, 26, 57, 38, 13, 49, 10, 21, 44, 21, 55, 21, 12]
# count = 0
# for i in range(0, len(a)):
#     count = 0
#     for j in range(0, len(a)):
#         if a[i] == a[j]:
#             count = count + 1
#     if count >= 3:
#         print(a[i])
# a = [18, 21, 13, 34, 13, 65, 26, 57, 38, 13, 49, 10, 21, 44, 21, 55, 21, 12]
# for i in range(0, len(a)):
#     b = a.count(a[i])
#     if b >= 3:
#         print(a[i], end=" ")
# a = [18, 21, 13, 34, 13, 65, 26, 57, 38, 49, 10, 44, 55, 12]
# a = [3, 4, 2, 13, 15, 22, 34, 23, 31, 41]
# b = sum(a)
# average = b / len(a)
# print(average)
# a = [12, 32, 42, 87, 65]
# b = [21, 33, 100, 51, 99, 76]
# c = []
# c.extend(a)
# c.extend(b)
# c.sort()
# c.reverse()
# print(c)
# a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# sum = 0
# for i in range(1, len(a) - 1):
#     sum = sum + a[i]
# print(sum)
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
b = []
for i in range(0, 10):
    if a[i] % 2 != 0:
        b.append(a[i])
print(b)
