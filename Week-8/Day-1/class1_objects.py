class Student:
    # data members
    # name = ""
    # age = 0
    # gender = ""

    # methods
    def greet(self):
        print(f"your name is {self.name}")
        print(f"your age is {self.age}")
        print(f"your gender is {self.gender}")

    def getdata(self):
        self.name = input("ENter your name = ")
        self.age = input("ENter your age = ")
        self.gender = input("ENter your gender = ")
        self.city = input("Enter your city =")


s1 = Student()
s1.getdata()
s1.greet()
