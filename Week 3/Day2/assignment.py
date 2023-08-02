# n = int(input("Enter the number = "))
# fact = 0
# for i in range(1, n):
#     for j in range(1, n):
#         if i % j == 0:
#             fact = fact + 1
#         if fact == 2:
#             print(i)
# a = [12, 3, 54, 8, 23, 87, 1, 99]
# a.sort()
# print(f"Minumum value is {a[0]}")
# print(f"Maximum value is {a[-1]}")
# a = [3, 4, 2, 3]
# b = sum(a)
# average = b / len(a)
# print(average)
# print(len(a))
# print(b)
n = int(input("Enter number = "))
count = 0
for i in range(0, n + 1):
    fact = 0
    for j in range(1, n + 1):
        if i % j == 0:
            fact = fact + 1
    if fact == 2:
        count = count + 1
        print(i)

print(count)
