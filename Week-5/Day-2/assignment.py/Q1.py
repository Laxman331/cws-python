"""Q1. Write a Python program to check if a string has at least one
letter and one number. If it has at least one letter and one number
then print YES else print NO."""


# a = "Laxman1"
# b = list(a)
# count = 0
# for i in b:
#     if i == b :
#         count = count + 1
# print(count)
user_string = input("Enter a sentence = ")

isLetter = False
isNumber = False

for i in user_string:
    if i.isdigit():
        isNumber = True
    elif i.isalpha():
        isLetter = True

if isNumber == True and isLetter == True:
    print("Both number and letter exists")
else:
    print("Both number and letter does not exists")
