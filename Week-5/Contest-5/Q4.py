"""Q4. Write a python program to convert Snake case to Pascal case.
Ask string from user.
Example input: aeroplane_is_a_good_transport
Example output: AeroplaneIsAGoodTransport
Example input: we_are_learning_python
Example output: WeAreLearningPython"""

a = input("Enter a string =")
b = a.split("_")
c = "".join(i for i in b)
print(c.upper())
