a = {"eng": 10, "maths": 82, "sci": 85}
keyname = input("Enter key name present in the dictionary = ")
if a.get(keyname) != None:
    a.pop(keyname)
    print(a)
else:
    print("key does not exist")
