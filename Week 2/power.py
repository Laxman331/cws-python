"""
Enter a number = 5
Enter power = 3
(5*5*5)

Result = 123

Enter a number = 2
Enter power = 8
(2*2*2*2*2*2*2*2)

Result = 256
"""
num = int(input("Enter number = "))
power = int(input("Enter power = "))
i = 1
result = 1
while i <= power:
    result = result * num
    i = i + 1
print(result)
