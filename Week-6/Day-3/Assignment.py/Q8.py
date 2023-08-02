"""Q8. Write a function prodDigits() that inputs a number and prints
the product of digits of that number"""


def prodDigits(a):
    b = a % 10
    c = a // 10
    print(b * c)


prodDigits(33)
