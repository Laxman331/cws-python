a = {"eng": 71, "maths": 82, "sci": 31, "soc": 16, "hin": 89}
b = {}
for k, v in a.items():
    if v >= 33:
        b[k] = "pass"
    else:
        b[k] = "fail"
print(b)
