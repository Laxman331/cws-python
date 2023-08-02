"""Q3. Write a Python class named BankAccount with two instance
variables balance and accountNumber. Write methods named
deposit and withdraw that allow the user to deposit or withdraw
money from the account"""
import random


class BankAccount:
    Balance = 0
    account_number = random.randint(1000, 9999)

    def datadisplay(self):
        print(f"Your account number is ={self.account_number}")
        print(f"your intial balance is {self.Balance}")

    def deposit(self):
        amount = int(input("Enter amount to deposit = "))
        self.Balance = self.Balance + amount
        return f"Account balance is {self.Balance}"

    def withdrawal(self):
        amount = int(input("Enter amount to withdrawal = "))
        if amount > self.Balance:
            return f"Insufficient balance. Your actual balance is {self.Balance}"
        else:
            self.Balance = self.Balance - amount
            return f"Account balance is {self.Balance}"


customer1 = BankAccount()
customer1.datadisplay()
print(customer1.deposit())
print(customer1.withdrawal())
