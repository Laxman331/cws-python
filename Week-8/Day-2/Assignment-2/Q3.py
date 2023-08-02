"""Q3. Write a Python class named Rectangle with a constructor that
takes no arguments and prompts the user for the length and width
of the rectangle. The constructor should initialize two instance
variables with the same names. Write a method named area that
calculates and returns the area of the rectangle."""


class Rectangle:
    length = 0
    breadth = 0

    def inputdimensions(self):
        self.length = int(input("Enter length of rectangle = "))
        self.breadth = int(input("Enter breadth of rectangle = "))

    def Area(self):
        return f"area is {self.length*self.breadth}"


a = Rectangle()
a.inputdimensions()
print(a.Area())
