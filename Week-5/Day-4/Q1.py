# a = "aeroplane is a good mode of transport good bye ok done"
# b = a.split()
# print(b)
# for i in b[0::2]:
#     print(i, end=" ")


# a = "aeroplane ok is a good mode of a transport good bye ok done"
# b = a.split()
# c = []
# for i in b:
#     if i not in c:
#         c.append(i)
# print(c)

"""a = "aeroplane ok is a good mode of a transport good bye ok done"
b = a.split()
print(b)
for i in b[-1::-1]:
    print(i[-1::-1], end=" ")"""
a = ""
b = False
for i in a:
    if i.isalnum:
        b = True
if b == True:
    print("ne")
else:
    print("e")
