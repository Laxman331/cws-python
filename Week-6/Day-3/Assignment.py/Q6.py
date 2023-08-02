"""Q6. Write a Python function to create and print a list where the
values are square of numbers between 1 and 30 (both included)"""


def createlist():
    a = []
    for i in range(1, 31):
        a.append(i * i)
    print(a)


createlist()
