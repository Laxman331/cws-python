"""Q5. Write a Python program to check if a string is an isogram (no
repeating characters).
Example 1:
Input: "python"
Output: Yes, the string is an isogram.
Example 5:
Input: "book"
Output: No, the string is not an isogram."""

a = input("Enter a string =")
b = list(a)
count = 0
for i in b:
    c = b.count(i)
    if c > count:
        count = c
if count == 1:
    print("Yes, the string is an isogram.")
else:
    print("No, the string is not an isogram.")
