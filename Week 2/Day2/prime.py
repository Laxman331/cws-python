# n = int(input in range(1, 10))
div = 0
for n in range(1, 10):
    for i in range(1, 10):
        if n % i == 0:
            div = div + 1
            # print(div)
            # if div <= 2:
            #     print("Prime Number")
            print(div)
            if div <= 2:
                print("Prime number")
                print(n)
