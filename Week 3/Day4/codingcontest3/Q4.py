"""Q4. Given a list of integers, write a program to find the sum of all positive numbers and the product of all negative numbers."""

a = [2, -2, 6, -3, 18, 0, -12, 82, -3]
sum = 0
product = 1
for i in a:
    if i > 0:
        sum = sum + i
    elif i == 0:
        continue
    else:
        product = product * i
print(f"sum of positive numbers is {sum}")
print(f"product of negative numbers is {product}")
