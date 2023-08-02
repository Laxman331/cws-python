"""Q4. Write a function called count_vowels(s) that takes a string s
as a parameter and returns the total number of vowels (a, e, i, o, u)
in the string."""


def count_vowels(s):
    count = 0
    total_no_of_vowels = []
    for i in s:
        if i in "aeiou":
            count = count + 1
            total_no_of_vowels.append(i)
    return count and tuple(total_no_of_vowels)


x = count_vowels("aeroplane")
print(x)
