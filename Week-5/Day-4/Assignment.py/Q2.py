"""Q2. Write a Python program to find the length of the longest word in a string.
Example 1:
Input: "The quick brown fox jumps over the lazy dog"
Output: Length of the longest word: 5
Example 2:
Input: "I love coding in Python"
Output: Length of the longest word: 6"""

a = input("enter a sentence =")
b = a.split()
max = 0
for i in b:
    if len(i) > max:
        max = len(i)
print(max)
