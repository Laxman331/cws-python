if True:
    print("Enter 1 to add contacts")
    print("Enter 2 to delete contacts")
    print("Enter 3 to search contacts")
    print("Enter 4 to display all contacts")

contacts = [
    ["laxman", 908298, "laxman@gmail.com"],
    ["man", 903249, "man@gmail.com"],
    ["lax", 9048281, "lax@gmail.com"],
]

# delete_contact = input("Enter contact name to delete = ")
# for c in contacts:
#     if delete_contact == c[0]:
#         contacts.pop(c)

# print(contacts)

for c in contacts:
    del c
print(contacts)
