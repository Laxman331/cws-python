# a = [12, 54, 87, 64, 32, 28]
# sum = 0
# for i in range(0, len(a)):
#     if a[i] % 3 == 0:
#         sum = sum + a[i]
# print(sum)
# a = [15, -8, 24, 45, -18, -3, 23, -76, 9, 0]
# positive = 0
# negative = 0
# Zero = 0
# for i in range(0, len(a)):
#     if a[i] > 0:
#         positive = positive + 1
#     elif a[i] == 0:
#         Zero = Zero + 1
#     else:
#         negative = negative + 1
# print(f"positive numbers are {positive}")
# print(f"negative numbers are {negative}")
# print(f"Zeros are {Zero}")
# a = [11, 22, 33, 48, 65, 62, 74, 56, 99]
# for i in range(len(a) - 1, -1, -1):
#     print(a[i], end=" ")
a = [45, 12, 59, 60, 47, 3412, 3111]
for i in range(0, len(a)):
    if i % 2 == 0:
        print(a[i], end=" ")
