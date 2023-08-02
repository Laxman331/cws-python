Accounts = [11, 22, 33, 44, 55]


# def searchAccount(AccountNumber):
#     for i in Accounts:
#         if 11 == AccountNumber:
#             return i
#     else:
#         return None

for i in Accounts:
    if (i == 11) or (i == 55):
        print(i)
    break
else:
    print("Not found")
