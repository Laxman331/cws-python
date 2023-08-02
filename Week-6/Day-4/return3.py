def sum(a: list):
    sum = 0
    for i in a:
        sum = sum + i
    return sum


x = [10, 20, 30]
sum(x)


def check(n):
    if n % 2 == 0:
        print("even")
    else:
        print("odd")


check(sum(x))
