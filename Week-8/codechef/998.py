# a = 987 % 10
# b = 987 // 10
# print(b)
# print(a)


n = int(input())
count = 0
while n > 0:
    a = n % 10
    if a == 4:
        count = count + 1
    n = n // 10
print(count)
