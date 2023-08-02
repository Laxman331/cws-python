"""Q3. Write a function called filter_even_numbers(lst) that takes a
list of integers lst as a parameter and returns a new list containing
only the even integers from the input list."""


def filter_even_numbers(a: list):
    b = []
    for i in a:
        if i % 2 == 0:
            b.append(i)
    return b


x = filter_even_numbers([12, 26, 31, 47, 98, 77, 64])
print(x)
