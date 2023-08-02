"""Q1. Write a Python class named Rectangle with two variables
length and width. Write a method named area that calculates
and returns the area of the rectangle."""


class Rectangle:
    length = 0
    breadth = 0

    def inputdimensions(self):
        self.length = int(input("Enter length of rectangle = "))
        self.breadth = int(input("Enter breadth of rectangle = "))

    def Area(self):
        return f"Area of Rectangle is = {self.length*self.breadth}"


s1 = Rectangle()
s1.inputdimensions()
print(s1.Area())
