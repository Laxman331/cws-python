import datetime
import time

a = []

t1 = datetime.datetime.now()
a = [i for i in range(1, 50000001)]
# for i in range(1, 50000001):
#     a.append(i)

t2 = datetime.datetime.now()
print(t2 - t1)
