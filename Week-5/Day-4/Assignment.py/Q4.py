"""Q4. Write a Python program to remove duplicate characters from
a string and return the modified string.
Example 1:
Input: "hello"
Output: Modified string: helo"""

a = input("Enter a string =")
b = list(a)
c = []
for i in b:
    if i not in c:
        c.append(i)
print("".join(i for i in c))
