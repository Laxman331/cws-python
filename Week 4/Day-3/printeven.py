"""
Put 5 subject name and marks in a dictionary.
Print the total of all marks divisible by 2.
"""
a = {"eng": 71, "maths": 82, "sci": 90, "soc": 96, "hin": 89}
total = 0
for i in a:
    if a.get(i) % 2 == 0:
        total = total + a.get(i)
print(total)
