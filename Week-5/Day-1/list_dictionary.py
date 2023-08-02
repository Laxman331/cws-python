a = {
    "sagar": [67, 74, 32, 12, 94],
    "sanjay": [76, 32, 12, 34, 33],
    "akul": [76, 888, 32, 4, 56],
}
c = []
k = 0
for k, v in a.items():
    c.extend(v)
print(max(c))
for k, v in a.items():
    if max(c) in v:
        print(k)
# max = 0
# for k, v in a.items():
#     for i in v:
#         if i > max:
#             max = i
# print(f" {max}")
# max = []
# for k, v in a.items():
#     max.append(v)
# print(max)
