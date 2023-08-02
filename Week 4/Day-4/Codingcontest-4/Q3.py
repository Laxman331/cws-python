"""Q3. Write your own dictionary. Then ask a number from a user.
Create a new dictionary with only those key-value pairs having
value greater than those number.
a = {"a": 10, "b": 5, "c": 15, "d": 3}
Enter a number = 8
Output: {"a": 10,"c": 15}"""

a = {"a": 10, "b": 5, "c": 15, "d": 3}
b = {}
n = int(input("Enter number = "))
for k, v in a.items():
    if v > n:
        b[k] = v
print(b)
