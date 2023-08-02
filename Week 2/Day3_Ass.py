# start = int(input("Enter start number = "))
# end = int(input("Enter end number = "))
# for i in range(start, end + 1):
#     print(i)
# start = int(input("Enter start number = "))
# end = int(input("Enter end number = "))
# for i in range(start, end + 1):
#     if i % 5 == 0 or i % 7 == 0:
#         print(i)
# start = int(input("Enter start number = "))
# end = int(input("Enter end number = "))
# sum = 0
# for i in range(start, end + 1):
#     if i % 4 == 0:
#         sum = sum + i
# print(sum)
# mul = 1
# for i in range(1, 11):
#     mul = mul * i
# print(mul)
# n = int(input("Enter number = "))
# for i in range(1, 11):
#     mul = n * i
#     print(mul)
# count = 0
# for i in range(20, 71):
#     if i % 4 == 0:
#         count = count + 1
# print(count, end=" ")
n = int(input("Enter number = "))
div = 0
for i in range(1, n + 1):
    if n % i == 0:
        div = div + 1
if div <= 2:
    print("prime number")
else:
    print("not a prime number")
