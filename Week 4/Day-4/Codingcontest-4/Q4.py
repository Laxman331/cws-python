"""Q4. Make 2 dictionary dict1 and dict2. Write a new dictionary
containing the keys that are present in dict1 but not in dict2.
dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}
 Output ={'a': 1}"""

dict1 = {"a": 1, "b": 2, "c": 3}
dict2 = {"b": 3, "c": 4, "d": 5}
a = {}
for k, v in dict1.items():
    for k1, v1 in dict2.items():
        if k in dict1 and k not in dict2:
            a[k] = v
print(a)
