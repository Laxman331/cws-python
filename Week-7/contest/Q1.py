"""Q1. Write a Python program that takes a user's input for a file name
and reads the content of the file. The program should print the
total number of lines, words, and characters in the file.
Example input: file.txt
Example output: Lines: 5, Words: 20, Characters: 100"""
file_name = input("Enter file name =")
f = open(mode="r", file=file_name)
a = f.readlines()
b = []
for i in a:
    c = i.strip()
    b.append(c)
count = 0
for i in b:
    for j in i:
        count = count + 1
print(count)
print(f"No of lines ={len(a)},words ={len(a)} charcters in file is ={count}")
