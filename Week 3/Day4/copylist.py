a = [12, 32, 14, 15]
# b = a
# print(a)
# print(b)
# a[1] = 13
# print(a)
# print(b)
b = a.copy
print(a)
a[1] = 13
# print(a)
print(b)
a = [500]  # 500 address
b = a
# b=500

print(a)
print(b)

# a = [99, 33]  # 300
a[3] = 100
print(a)
print(b)