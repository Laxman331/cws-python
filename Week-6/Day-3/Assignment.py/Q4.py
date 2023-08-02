"""Q4. Write a Python program to reverse a string."""


def reverse(a):
    b = list(a)
    b.reverse()
    print("".join(i for i in b))


reverse("pot")
