class Student:
    # data members
    name = ""
    age = 0
    gender = ""

    # methods
    def greet(self):
        print(f"your name is {self.name}")
        print(f"your age is {self.age}")
        print(f"your gender is {self.gender}")


s1 = Student()
s1.name = "Laxman"
s1.age = 22
s1.gender = "male"
s1.greet()
# print(s1.name)
# print(s1.age)
# print(s1.gender)
s2 = Student()
s2.name = "kohili"
s2.age = 18
s2.gender = "male"
s2.greet()
# print(s2.age)
# print(s2.name)
# print(s2.gender)
