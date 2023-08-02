T = int(input())
for i in range(0, T):
    n = int(input())
    count = 0
    while n > 0:
        a = n % 10
        if a == 4:
            count = count + 1
        n = n // 10
    print(count)
