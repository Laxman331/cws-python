# a = "abacabad"
# for i in a:
#     count = 0
#     for j in a:
#         if i == j:
#             count = count + 1
#     if count == 1:
#         print(i)
#         break
"""Q1. Write a function to find the first non-repeating character in a
string.
Example 1:
Input: "abacabad"
Output: "c"
Explanation: The first non-repeating character in the string is "c". It appears
only once and is the first character that does not repeat.
Example 2:
Input: "leetcode"
Output: "l"
Explanation: The first non-repeating character in the string is "l". It appears
only once and is the first character that does not repeat.
Example 3:
Input: "aabbcc"
Output: None
Explanation: In this case, there are no non-repeating characters in the string.
All characters repeat at least once, so the output is None."""


def non_repeating_character(a):
    for i in a:
        count = 0
        for j in a:
            if i == j:
                count = count + 1
        if count == 1:
            print(i)
            break
    else:
        print("None")


x = input("Enter a string =")
non_repeating_character(x)
