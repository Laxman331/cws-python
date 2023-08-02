"""Q4. Write a Python program that takes a user's input for a file
name and a word. The program should read the content of the file
and find the line number where the given word first appears. If the
word is not found in the file, print a message indicating this. Use
exception handling to deal with non-existent files.
Enter file name: file.txt
Enter word to search: hello
Example output: The word"hello" first appears on line 3."""
try:
    file_name = input("Enter file name =")
    word = input("Enter a word =")
    f = open(mode="r", file=file_name)
    a = f.readlines()
    b = []
    for i in a:
        c = i.strip()
        b.append(c)
    line = 0
    for i in range(0, len(b)):
        if b[i] == word:
            line = i + 1
    if line == 0:
        print("Word is not found in a file")
    else:
        print(f"The word {word} first appears on line {line}")
except:
    print("file does not exist")
