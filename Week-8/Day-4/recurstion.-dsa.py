def add(n):
    if type(n) != int or n < 1:
        return "Wrong input"
    else:
        if n == 1:
            return 1
        else:
            return n + add(n - 1)


x = add(5)
print(x)
