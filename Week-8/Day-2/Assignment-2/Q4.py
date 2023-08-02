"""Q4. Write a Python class named BankAccount with a constructor
that takes no arguments and prompts the user for an initial
balance and an account number. The constructor should initialize
two instance variables, balance and accountNumber. Write
methods named deposit and withdraw that allow the user to
deposit or withdraw money from the account."""
import random


class Bank:
    def __init__(self):
        self.amount = 0
        self.accno = 0

    def getdata(self):
        self.accno = random.randint(10000, 99999)
        print(f"Your account number is ={self.accno}")
        self.amount = int(input("Enter amount = "))

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


a = Bank()
a.getdata()
a.deposit()
a.withdraw()
