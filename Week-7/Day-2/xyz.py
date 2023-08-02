import area

x = area.square(6)
x = area.circle(8)
x = area.rectangle(8, 6)

from area import rectangle

x = rectangle(3, 9)

from area import *

x = rectangle(3, 9)
print(x)
x = square(3)
print(x)
x = circle(9)
print(x)
