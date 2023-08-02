phy = int(input("enter phy marks out of 100 = "))
chem = int(input("enter chem marks out of 100 = "))
comp = int(input("enter comp marks out of 100 = "))
eng = int(input("enter eng marks out of 100 = "))
his = int(input("enter his marks out of 100 = "))
total_marks = phy + chem + comp + eng + his
percentage = (total_marks * 100) / 500
print(f"your total is {total_marks}")
print(f"your percentage is {percentage}")
if percentage >= 33:
    print("Pass")
else:
    print("fail")
