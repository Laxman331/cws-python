# try:
#     a = int(input("Enter number1 = "))
#     b = int(input("Enter number2 = "))
#     print(a + b)
# except Exception as e:
#     print(e)

try:
    username = input("Enter username = ")
    password = input("Enter password = ")
    if username == "admin" and password == "admin":
        print("Sucessful")
    else:
        raise Exception("some error occured")
except Exception as e:
    print(e)
