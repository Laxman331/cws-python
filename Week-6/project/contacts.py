"""1.	Use lists to store contact information, such as names, phone numbers, and email addresses.
2.	Allow users to add, delete, and search for contacts.
3.	Use conditional statements to search for specific contacts.
4.	Use loops to display all contacts or iterate through the list for various operations.

Instructions:
1.	Create a data structure to store contact information, including names, phone numbers, and email addresses.
2.	Implement a menu-driven interface to allow users to choose between adding, deleting, searching for, or displaying all contacts.
3.	To add a contact, allow users to input the contact's name, phone number, and email address. Store this information in the data structure.
4.	To delete a contact, allow users to input the contact's name. Use a conditional statement to find the contact in the data structure and remove it.
5.	To search for a contact, allow users to input the contact's name. Use a conditional statement to find and display the contact's information"""

contacts = []


if 1 == 1:
    print("Enter 1 to add contacts")
    print("Enter 2 to delete contacts")
    print("Enter 3 to search contacts")
    print("Enter 4 to display all contacts")

user_choice = int(input("Enter your choice = "))

if user_choice == 1:
    "Add contact"
    name = input("Enter your contact name = ")
    phone_number = int(input("Enter your phone number = "))
    email = input("Enter your Email id = ")
    c = [name, phone_number, email]
    contacts.append(c)
elif user_choice==2:
     "To delete contact"
     delete_contact=input("Enter contact name to delete = ")
     for c in contacts:
         for i in range(1,len(contacts)):
             if c[i]==delete_contact:
                 contacts.pop(c[i])
   
