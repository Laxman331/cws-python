a = {"eng": 80, "maths": 82}
# del a["eng"]
# print(a)
# del a
keyname = input("Enter key name = ")
if a.get(keyname) != None:
    print(a[keyname])
else:
    print("key name does not exist")
