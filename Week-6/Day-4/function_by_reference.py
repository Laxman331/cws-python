# def num1(a):
#     a = a + 10
#     print(f"inside function {a}")


# x = 20
# print(f" function {x}")
# num1(x)
# print(f"outside function {x}")


def xyz(a: list):
    a.append(30)
    print(f"inside function {a}")


x = [12, 23, 34, 56, 87]
print(f" function {x}")
xyz(x)
print(f"outside function {x}")

'''only in LIST and DICTIONARY inside function will come in outside function'''
