start = int(input("enter number = "))
end = int(input("enter number = "))
count = 0
while start <= end:
    if start % 5 == 0:
        count = count + 1
    start = start + 1
print(count)
"""
Ask a number from user = 

54653
Count the number of digits = 5

122111
Count the number of digits = 6

//
"""