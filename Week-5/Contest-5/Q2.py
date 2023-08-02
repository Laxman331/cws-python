"""Q2. Write a python program to capitalize the first and last
character of each word in a string entered by user.
Example input: hello world
Example output: HellO WorlD

Example input: aeroplane is better
Example output: AeroplanE IS BetteR"""

# user_string = input("Enter a sentence = ")
user_string = "aerOPLAne is a good transport"

words = user_string.split()

for i in words:
    if len(i) == 1:
        print(i.upper(), end=" ")
    else:
        print(i[0].upper() + i[1 : len(i) - 1] + i[-1].upper(), end=" ")
