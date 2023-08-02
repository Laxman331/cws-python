# n = int(input("Enter number = "))
# for i in range(1, 20):
#     if n % i == 0:
#         print(i)

n = int(input("Enter number = "))
count = 0
for i in range(1, n + 1):
    if n % i == 0:
        count = count + 1
        print(i)
print(count)
