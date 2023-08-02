class Student:
    def __init__(self):
        self.name = input("Enter name = ")
        self.age = int(input("Enter age = "))
        self.gender = input("Enter gender = ")

    def greet(self):
        print(f"Your name is {self.name}")
        print(f"Your age is {self.age}")
        print(f"Your gender is {self.gender}")


s1 = Student()
print("_______")
s1.greet()
s2 = Student()
s2.greet()
