"""Q1. Write a Python class named Book with a constructor that takes
a title, an author, and a price as arguments and initializes three
instance variables, title, author, and price. Write a method named
discount that applies a discount to the price and returns the
discounted price."""


class Book:
    def __init__(self):
        self.title = input("Enter Title of the Book =")
        self.author = input("Enter author of the Book =")
        self.price = int(input("Enter price of the Book ="))

    def discount(self):
        discount = int(input("Enter discount percentage on the book = "))
        discount_amount = self.price * ((discount) / 100)
        self.price = self.price - discount_amount
        print(f"Final price of the book after discount ={self.price}")


mind = Book()
mind.discount()
