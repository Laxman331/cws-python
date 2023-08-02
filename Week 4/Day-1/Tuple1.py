""" list is Mutable
Tuple is imutabel ( we cannot edit)
tuple represents in parenthesis()"""
a = (1, 2, 34, 76, 34, 98)
r = a.count(34)
print(r)

b = a.index(76)
print(b)

# Tuple vs List
"""
List is Mutable
Tuple is Immutable
"""
a = (45, 32, 12, 3, 33)

# genders = ("Male", "Female", "Others")
print(a)
print(type(a))

# a[0] = 100
# print(a)

# r = a.count(100)
# print(r)

# r = a.index(32)
# print(r)

for i in a:
    print(i)
