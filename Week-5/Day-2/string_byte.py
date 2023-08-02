a = input("enter a name = ")
"""sum = 0
for i in a:
    sum = sum + ord(i)
print(sum)"""
print(sum(ord(i) for i in a))
