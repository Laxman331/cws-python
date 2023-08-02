"""Q6. Write a Python program to find the most frequent word in a
string.
Example 1:
Input: "The quick brown fox jumps over the lazy dog".
Output: Most frequent word: the"""

a = input("Enter a string =")
b = a.split()
c = {}
for i in b:
    count1 = b.count(i)
    c[i] = count1
d = list(c.values())
for k, v in c.items():
    if v == max(d):
        print(k)
        break
