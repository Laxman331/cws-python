"""Q3. Write a Python program to combine two dictionary by adding
values for common keys.
d1 = {"a": 100, "b": 200, "c":300}
d2 = {"a": 300, "b": 200, "d":400}
Sample output: Counter("a": 400, "b": 400, "d": 400, "c": 300})"""

d1 = {"a": 100, "b": 200, "c": 300}
d2 = {"a": 300, "b": 200, "d": 400}
c = {}
c.update(d1)
c.update(d2)
for k in d1:
    if k in d2:
        c[k] = d1.get(k) + d2.get(k)
print(c)
