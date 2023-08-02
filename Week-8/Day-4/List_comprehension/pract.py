# a = [i for i in range(1, 46) if 45 % i == 0]
# print((a))

n = int(input("Enter number="))
a = ["prime" if len([i for i in range(1, n + 1) if n % i == 0]) == 2 else "Np"]
print(a)
