"""Q6. There is a list which contains both strings and integers. Count the number of strings and integers present in the list."""

a = [12, "s", 2, "a", -4, "y", "abc", 0, "t", "xyz", 76]
integers = 0
strings = 0
for i in a:
    if i == str(i):
        strings = strings + 1
    else:
        integers = integers + 1
print(f" Number of strings present in the list is {strings}")
print(f" Number of integers present in the list is {integers}")
