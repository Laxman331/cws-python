# a = [1, 2, 4, 5]

# for i in range(min(a), max(a) + 1):
#     if i not in a:
#         print(i)

"""Q4. Implement a function to find the missing number in a given
range of integers.
Example 1:
Input: [1, 2, 4, 6, 3, 7, 8]
Output: 5
Explanation: In the given range of integers from 1 to 8, the number 5 is missing.
Example 2:
Input: [10, 12, 11, 14, 13, 15]
Output: None
Explanation: In this case, there are no missing numbers in the given range of
integers from 10 to 15."""


def missingnumber(a: list):
    for i in range(min(a), max(a) + 1):
        if i not in a:
            print(i)
            break
    else:
        print("None")


a = [1, 2, 4]
missingnumber(a)
