"""Q3. Write a Python program to find the most common character in
a string. (Print the letter which repeats most of the time)
Example 1:
Input: "hello"
Output: Most common character: l
Example 2:
Input: "programming"
Output: Most common character: g
"""
a = input("enter charcter =")
b = list(a)
count = 0
char = " "
for i in b:
    c = b.count(i)
    if c > count:
        count = c
        char = i
print(char)
