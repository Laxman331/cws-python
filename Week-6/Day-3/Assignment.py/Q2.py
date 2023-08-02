"""Q2. Write a Python function to multiply all the numbers in a list."""


def multiplicationoflist(a):
    mul = 1
    for i in a:
        mul = mul * i
    print(f"multiplication of list {mul}")


multiplicationoflist([11, 2, 3, 5])
