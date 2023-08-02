# num = int(input("Enter number "))
# if num % 3 == 0:
#     print("Divisble by 3")
# else:
#     print("Not Divisble by 3 ")
# num = int(input("Enter number = "))
# if num % 2 == 0:
#     print("Even Number")
# else:
#     print("Odd Number")
# length = int(input("Enter length of a rectangle = "))
# breadth = int(input("Enter breadth of a rectangle = "))
# if length == breadth:
#     print("It is a Square ")
# else:
#     print("It is not a Square ")
# marks = int(input("Enter marks = "))
# if marks > 80:
#     print("Grade is A ")
# elif marks >= 60 and marks <= 80:
#     print("Grade is B ")
# elif marks >= 50 and marks < 60:
#     print("Grade is c ")
# elif marks >= 45 and marks < 50:
#     print("Grade is D ")
# elif marks >= 25 and marks < 45:
#     print("Grade is E ")
# elif marks < 25:
#     print("Grade is F ")
no_of_classes_held = int(input("Enter no of classes held = "))
no_of_classes_attended = int(input("Enter no of classes attended = "))
percentage_of_class_attended = (no_of_classes_attended * 100) / no_of_classes_held
print(f"percentage of class attended = {percentage_of_class_attended}")
if percentage_of_class_attended >= 75:
    print("Student allowed to sit in the exam ")
else:
    print("Not allowed to sit in the exam")
