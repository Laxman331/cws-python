"""Q5. Write a Python function that checks whether a passed string is
palindrome or not."""


def palindrome(a):
    b = list(a)
    b.reverse()
    if ("".join(i for i in b)) == a:
        print("palindrome")
    else:
        print("Not a palindrome")


palindrome("madam")
