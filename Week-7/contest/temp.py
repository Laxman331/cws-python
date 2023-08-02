# f = open("abc.txt", "r")
# a = f.read()
# print(a)
# for i in a:
#     print(i)
n = input("enter =")
b = ["hello how are you", "goodmorning", "bye"]
line = 0
for i in range(0, len(b)):
    if b[i] == n:
        line = i + 1
    else:
        for j in b[i]:
            if j == n:
                line = i + 1
print(line)
