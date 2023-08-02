a = {"eng": 71, "maths": 82, "sci": 31, "soc": 16, "hin": 89}
b = {}
for k, v in a.items():
    v = v + 5
    b[k] = v
print(b)
