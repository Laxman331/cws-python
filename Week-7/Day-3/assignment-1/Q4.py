"""Q4. Take an input from user. Check if the number is prime or not. If
number is not prime, raise your own exception. Remember to
handle all other exceptions."""

try:
    n = int(input("Enter number = "))
    div = 0
    for i in range(1, n + 1):
        if n % i == 0:
            div = div + 1
    if div == 2:
        print("Prime number")
    else:
        print("not a prime number")
except ValueError:
    print("please enter integer")
except:
    print("some error occured")
