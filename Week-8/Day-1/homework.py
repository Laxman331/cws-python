"""
Rectangle - Class

inputDimension()
    Ask user - Length, Breadth

area()
    print Area

parameter()
    print parameter


a,b,c
r1,r2,r3
"""


class Rectangle:
    length = 0
    breadth = 0

    def inputdimensions(self):
        self.length = int(input("Enter length of rectangle = "))
        self.breadth = int(input("Enter breadth of rectangle = "))

    def Area(self):
        print(f"area is {self.length*self.breadth}")

    def permeter(self):
        print(f"permeter  is {2*(self.length+self.breadth)}")


a = Rectangle()
a.inputdimensions()
a.Area()
a.permeter()
print("---------")

b = Rectangle()
b.inputdimensions()
b.Area()
b.permeter()
print("---------")

c = Rectangle()
c.inputdimensions()
c.Area()
c.permeter()
