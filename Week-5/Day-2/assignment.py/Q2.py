"""Q2. Write a python program to ask a string from user. Then count
the number of vowels and number of consonants in that string.
(Make sure there are no spaces in string when you enter in
terminal)."""

a = input("Enter a string =")
b = ["a", "e", "i", "o", "u"]
count_vowels = 0
count_consonants = 0
for i in a:
    if i in b:
        count_vowels = count_vowels + 1
    else:
        count_consonants = count_consonants + 1
print(f"no of vowels = {count_vowels}")
print(f"no of consonants= {count_consonants}")
