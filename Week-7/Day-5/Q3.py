"""Q3. Ask a word from user. Count the frequency of how many times
that number comes in a file."""
f = open("xyz.txt", "r")
a = f.readlines()
b = []
for i in a:
    p = i.strip()
    b.append(p)
print(b)
word = input("Enter word =")
if word in b:
    print(b.count(word))

