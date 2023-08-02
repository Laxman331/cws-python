"""Q5. Write a function called is_palindrome(s) that takes a string s
as a parameter and returns True if the string is a palindrome
(reads the same forward and backward), otherwise False."""


def is_palindrome(s):
    b = list(s)
    b.reverse()
    if ("".join(i for i in b)) == s:
        return True
    else:
        return False


x = is_palindrome("racecar")
print(x)
