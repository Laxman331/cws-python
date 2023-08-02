"""Q5. Write a function called is_prime(n) that takes an integer n as
a parameter and returns True if the number is prime, otherwise
False."""


def is_prime(n):
    div = 0
    for i in range(1, n + 1):
        if n % i == 0:
            div = div + 1
    if div == 2:
        return True
    else:
        return False


a = is_prime(5)
print(a)
