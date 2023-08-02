"""Q7. Write a function that inputs a number and prints the
multiplication table of that number."""


def table(a):
    for i in range(1, 11):
        print(a * i, end=" ")


table(9)
