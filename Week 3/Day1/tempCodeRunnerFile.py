# n = int(input("Enter number = "))
# s = 0
# for i in range(1, n + 1):
#     if n == (i * i):
#         s = 1
# if s == 1:
#     print("Perfect Square")
# else:
#     print("Not a Perfect Square")
n = int(input("Enter number = "))
sum = 0
while n > 0:
    a = n % 10
    sum = sum + a
    n = n // 10
print(sum)
