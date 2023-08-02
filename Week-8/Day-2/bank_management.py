"""
Bank
    New object create (Constructor)
        amount=0
        account_no=randomly
        name=input
        bank_name

    Withdraw
    Deposit
    Display
    DisplayBalance
    Update
obj

"""
"""
Bank
    New object create (Constructor)
        amount=0
        account_no=randomly
        name=input
        bank_name

    Withdraw
    Deposit
    Display
    DisplayBalance
    Update
obj

"""
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


obj = Bank()
# obj2 = Bank()
obj.deposit()
a = [obj]
print(a[0].display())
# obj.display()
# obj2.display()
