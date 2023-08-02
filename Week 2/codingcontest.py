# for i in range(1, 21):
#     x = 10 * i
#     print(x, end=" ")
# x = 1
# for i in range(1, 10):
#     print(x, end=" ")
#     x = x * 10
# x = 1
# for i in range(1, 11):
#     print(x, end=" ")
# #     x = 1 * 1
# div = 0
# for n in range(1, 10):
#     for i in range(1, 10):
#         if n % i == 0:
#             div = div + 1
#         if div <= 2:
#             print(n, end=" ")
#         print(n, end=" ")
# sum = 0
# for i in range(1, 11):
#     sum = sum + (i * i)
# print(sum, end=" ")
# sum = 0
# n = int(input("Enter number = "))
# for i in range(0, n):
#     sum = sum + (1 / 2**i)
# print(sum, end=" ")
# sum = 1
# for i in range(1, 13):
#     print(sum, end=" ")
#     sum = sum * 2
# sum = 0
# n = int(input("Enter number = "))
# for i in range(0, n):
#     sum = sum + 1 / (2**i)
# print(sum, end=" ")
# div = 0
# n = int(input("Enter number= "))
# for n in range(1, 101):
#     div = 0
#     for i in range(1, 101):
#         if n % i == 0:
#             div = div + 1
#     if div == 2:
#         print(n, end=" ")
for i in range(1, 6):
    for j in range(1, i + 1):
        print(i, end=" ")
    print()
