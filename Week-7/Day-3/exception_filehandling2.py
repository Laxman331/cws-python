try:
    a = [1, 2, 36, 93, 14, 48, 64, "a"]
    print(a[2])
    print(a[0] / a[-1])
except ZeroDivisionError:
    print("number cannot be divided by 0")
except IndexError:
    print("given index is not there")
except:
    print("some error occured")
""""""
