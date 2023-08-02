"""Q1. Write a Python function to find the Maximum and minimum of
three numbers. Use 3 parameters."""


def maxandmin(a, b, c):
    if a > b and a > c:
        print(f"maximum is {a}")
    elif b > a and b > c:
        print(f"maximum is {b}")
    elif c > a and c > b:
        print(f"maximum is {c}")
    if a < b and a < c:
        print(f"minimum is {a}")
    elif b < a and b < c:
        print(f"minimum is {b}")
    elif c < a and c < b:
        print(f"minimum is {c}")


maxandmin(12, 22, 33)
