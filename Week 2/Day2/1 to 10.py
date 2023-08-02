# total = 0
# for i in range(1, 11):
#     total = total + i
# print(total)
# n = int(input("Enter an number: "))
# for i in range(1, n + 1):
#     if i%8==0:
#         print(i)
#     print(i, end=" ")
# n = int(input("Enter an number: "))
# for i in range(1, n + 1):
#     if i % 8 == 0:
#         print(i)
# n = int(input("Enter an number: "))
# count = 0
# for i in range(1, n + 1):
#     if i % 8 == 0:
#         count = count + 1
# print(count)
n = int(input("Enter an number: "))
count = 0
sum = 0
for i in range(1, n + 1):
    if i % 8 == 0:
        count = count + 1
        sum = sum + i
print(count)
print(sum)
