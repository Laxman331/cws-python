"""Q7. Write a function called merge_dictionaries(dict1, dict2) that
takes two dictionaries dict1 and dict2 as parameters and returns a
new dictionary that contains the key-value pairs from both input
dictionaries. If a key is present in both dictionaries, the value from
dict2 should overwrite the value from dict1."""


def merge_dictionaries(dict1, dict2):
    dict3 = {}
    dict3.update(dict1)
    dict3.update(dict2)
    return dict3


x = merge_dictionaries({"a": 2, "b": 3, "c": 2}, {"c": 4, "d": 5, "e": 6})
print(x)
