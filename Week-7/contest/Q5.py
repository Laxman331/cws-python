"""Q5. Write a Python program that takes a user's input for a file
name and a positive integer (n). The program should read the
content of the file and print the nth line. If the file has fewer lines
than the input integer, print a message indicating this. Use
exception handling to deal with non-existent files and invalid
inputs.
Enter file name: file.txt
Enter line: 5
Example output: Line 5: This is the fifth line of the file"""
try:
    file_name = input("Enter file name =")
    n = int(input("Enter a positive number ="))
    f = open(mode="r", file=file_name)
    a = f.readlines()
    b = []
    for i in a:
        c = i.strip()
        b.append(c)
    for i in range(0, len(b)):
        if i == (n - 1):
            print(b[i])
    if n > len(b):
        print("the file has fewer lines")
except:
    print("file does not exist")
