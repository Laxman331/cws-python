start = int(input("Enter start number = "))
end = int(input("Enter end number = "))
sum = 0
while start <= end:
    if start % 7 == 0:
        sum = sum + start
    start = start + 1
print(sum)
