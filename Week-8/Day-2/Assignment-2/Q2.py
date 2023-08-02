"""Q2. Write a Python class named Employee with a constructor that
takes a name, an age, a salary, and a department as arguments
and initializes four instance variables, name, age, salary, and
department. Write a method named promote that increases the
salary of the employee by a certain percentage."""


class Employee:
    def __init__(self):
        self.name = input("Enter your Name =")
        self.age = int(input("Enter your Age ="))
        self.salary = int(input("Enter your salary ="))
        self.department = input("Enter your Deparment =")

    def datadisplay(self):
        print(f"Employee Name is ={self.name}")
        print(f"Employee Age is ={self.age}")
        print(f"Employee Salary is ={self.salary}")
        print(f"Employee Department is ={self.department}")

    def promote(self):
        percentage = int(
            input("Enter how much percentage salary should be increased =")
        )
        Hike = self.salary * (percentage / 100)
        self.salary = self.salary + Hike
        print(f"Salary of a person after {percentage}% Hike is ={self.salary}")


a = Employee()
a.datadisplay()
a.promote()
