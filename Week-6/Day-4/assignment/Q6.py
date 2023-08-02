"""Q6. Write a function called find_common_elements(lst1, lst2)
that takes two lists lst1 and lst2 as parameters and returns a list
containing the common elements between the two lists."""


def find_common_elements(list1, list2):
    c = []
    for i in list1:
        if i in list2:
            c.append(i)

    return c


x = find_common_elements([10, 12, 14, 16, 19], [9, 10, 11, 12, 16, 20])
print(x)
