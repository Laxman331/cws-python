# num = int(input("Enter number = "))
# if num > 0:
#     print("Postive number")
# elif num < 0:
#     print("Negative  number")
# elif num == 0:
#     print(" Zero")
# character = input("Enter character = ")
# vowel = ["a", "e", "i", "o", "u"]
# if character in vowel:
#     print("Vowel")
# else:
#     print("consonant")
# num = int(input("enter number between 1 to 7 = "))
# if num == 1:
#     print("Monday")
# elif num == 2:
#     print("Tuesday")
# elif num == 3:
#     print("Wednesday")
# elif num == 4:
#     print("Thursday")
# elif num == 5:
#     print("Friday")
# elif num == 6:
#     print("Saturday")
# elif num == 7:
#     print("Sunday")
# else:
#     print("Invalid")
# num1 = int(input("enter number 1 = "))
# num2 = int(input("enter number 2 = "))
# num3 = int(input("enter number 3 = "))
# if num1 > num2 and num1 > num3:
#     print(f" Largest Number is {num1}")
# elif num2 > num1 and num2 > num3:
#     print(f" Largest Number is {num2}")
# elif num3 > num1 and num3 > num2:
#     print(f" Largest Number is {num3}")
num1 = int(input("Enter number 1  = "))
num2 = int(input("Enter number 2 = "))
print(f"Before Swaping; num1 is {num1} and num2 is {num2}")
num1, num2 = num2, num1
print(f" After Swaping;   num1 value  is {num1} and num2  value is {num2}")
num = int(input("enter number = "))
if num % 1 == 0 and num % num == 0:
    print("prime number")
