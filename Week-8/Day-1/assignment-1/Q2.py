"""Q2. Write a Python class named Car with two instance variables
make and model. Write a method named getMakeModel that
returns the make and model of the car as a string."""


class Car:
    make = 0
    model = 0

    def getdata(self):
        self.make = input("Enter Make of the car =")
        self.model = input("Enter Model of the car =")

    def getmakemodel(self):
        return f"your make is {str(self.make)} your Model is {str(self.model)}"


a = Car()
# a.getdata()
print(a.getmakemodel())
