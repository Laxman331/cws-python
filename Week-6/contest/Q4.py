"""Q4. Write a function called union_of_sets(set_a, set_b) that
takes two sets set_a and set_b as parameters and returns a new
set containing the union of the two input sets"""


def union_of_sets(a, b):
    c = a.union(b)
    return c


x = union_of_sets({1, 2, 3, 4}, {3, 4, 5, 6})
print(x)
