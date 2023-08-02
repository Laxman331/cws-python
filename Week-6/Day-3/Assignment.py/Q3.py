"""Q3. Ask a number from user. Pass that number as a parameter to
a function. Check if the number is prime or not."""


def prime(a):
    pass
    div = 0
    for i in range(1, a + 1):
        if a % i == 0:
            div = div + 1
    if div == 2:
        print("Given number is prime number ")
    else:
        print("given number is not a prime number")


prime(3)
