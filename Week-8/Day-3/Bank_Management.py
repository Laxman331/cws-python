import random


class Bank:
    def __init__(self):
        self.amount = 0
        self.accno = random.randint(100000, 999999)
        self.name = input("Enter your name = ")
        self.bankName = input("Enter your bank name = ")

    def display(self):
        print(f"\n-------INFO-------")
        print(f"Account number = {self.accno}")
        print(f"Balance = {self.amount}")
        print(f"Name = {self.name}")
        print(f"Bank name = {self.bankName}")

    def displayBalance(self):
        print(f"Your balance = {self.amount}")

    def deposit(self):
        newAmount = int(input("Enter amount to deposit = "))
        self.amount = self.amount + newAmount
        self.displayBalance()

    def withdraw(self):
        newAmount = int(input("Enter amount to withdraw = "))
        if newAmount > self.amount:
            print(f"Insufficient balance. Your actual balance is {self.amount}")
        else:
            self.amount = self.amount - newAmount
            self.displayBalance()

    def update(self):
        newName = input("Enter new name. Or if you want default leave blank = ")
        if newName != "":
            self.name = newName
        newBankName = input(
            "Enter new bank name. Or if you want default leave blank = "
        )
        if newBankName != "":
            self.bankName = newBankName


Accounts = []


def searchAccount(AccountNumber):
    for i in Accounts:
        if i.accno == AccountNumber:
            return i
    else:
        return None


while True:
    print("enter 1 to Add an account")
    print("enter 2 print all Accounts")
    print("enter 3 to search a Account")
    print("enter 4 to deposit  Account")
    print("enter 5 to Withdraw  Account")
    print("enter 6 to Check Balance")
    print("enter 7 to Transfer")

    choice = int(input("Enter your choice = "))
    if choice == 1:
        obj = Bank()
        Accounts.append(obj)
        print(Accounts)
    elif choice == 2:
        if len(Accounts) == 0:
            print("No Accounts there")
        else:
            for i in Accounts:
                i.display()
    elif choice == 3:
        Acc_no = int(input("Enter Account number = "))
        for i in Accounts:
            if i.accno == Acc_no:
                i.display()
                break
        else:
            print("No Account Found")
        break
    elif choice == 4:
        Acc_no = int(input("Enter Account number = "))
        for i in Accounts:
            if i.accno == Acc_no:
                i.deposit()
                break
        else:
            print("No Account Found")
    elif choice == 5:
        Acc_no = int(input("Enter Account number = "))
        for i in Accounts:
            if i.accno == Acc_no:
                i.withdraw()
                break
        else:
            print("No Account Found")
    elif choice == 6:
        Acc_no = int(input("Enter Account number = "))
        for i in Accounts:
            if i.accno == Acc_no:
                i.displayBalance()
                break
        else:
            print("No Account Found")
    elif choice == 7:
        acc_no = int(input("Enter Account Number ="))
        senderAccount = searchAccount(acc_no)
        if senderAccount != None:
            rec_accno = int(input("Enter Receiver Account Number ="))
            receiverAccountnumber = searchAccount(rec_accno)
            if receiverAccountnumber != None:
                transfer_amount = int(input("Enter Amount to transfer = "))
                if transfer_amount > senderAccount.amount:
                    print("Insufficient Balance")
                else:
                    receiverAccountnumber.amount += transfer_amount
                    senderAccount.amount -= transfer_amount
                    print(f"your Account Balance is ={senderAccount.amount}")
            else:
                print("Receiver Account Not Found")
        else:
            print("Account Doesn't Exist")
