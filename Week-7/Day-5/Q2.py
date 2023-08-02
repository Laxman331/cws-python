"""Q2. Ask a word from user. Print Yes or No if the word entered by
user exists in a file or not."""

f = open("xyz.txt", "r")
a = f.read()
word = input("Enter word =")
if word in a:
    print("yes")
else:
    print("no")
