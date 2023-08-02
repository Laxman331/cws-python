# a = [1, 2, 3, 4, 5]
# b = [4, 5, 6, 7, 8]
# c = []
# for i in a:
#     if i in b:
#         c.append(i)
# print(c)

"""Q2. Write a function to find the intersection of two arrays without
using sets.
Example 1:
Input: [1, 2, 3, 4, 5], [4, 5, 6, 7]
Output: [4, 5]
Example 2:
Input: [1, 2, 3, 4, 5], [6, 7, 8, 9]
Output: []
Example 3:
Input: [1, 2, 3, 4, 5], [5, 6, 7, 8]
Output: [5]"""


def intersection(a, b):
    c = []
    for i in a:
        if i in b:
            c.append(i)
    print(c)


a = [1, 2, 3, 4, 5]
b = [6, 4, 5, 7, 8]
intersection(a, b)
