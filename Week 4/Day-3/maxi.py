a = {"eng": 71, "maths": 96, "sci": 90, "soc": 82, "hin": 89}
max_marks = 0
sub = ""
for k, v in a.items():
    if v > max_marks:
        max_marks = v
        sub = k
print(max_marks)
print(sub)
# for i in a:
#     if a.get(i) > max_marks:
#         max_marks = a.get(i)
#         sub = i
# print(max_marks)
# print(sub)
