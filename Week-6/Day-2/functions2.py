def printnumber():
    start_num = int(input("enter start number = "))
    end_num = int(input("enter end number = "))
    sum = 0
    for i in range(start_num, end_num + 1):
        sum = sum + i
    print(f"sum is {sum}")


printnumber()
