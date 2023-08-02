"""Q4. Write a Python program that takes a user's input for a file
name and a word. The program should read the content of the file
and find the line number where the given word first appears. If the
word is not found in the file, print a message indicating this. Use
exception handling to deal with non-existent files.
Enter file name: file.txt
Enter word to search: hello
Example output: The word"hello" first appears on line 3."""
try:
    file_name = input("Enter file name = ")
    word = input("Enter the word = ").lower()  
    f = open(file_name, "r")
    lines = f.readlines()
    exists = False
    for i in range(0, len(lines)):
        if word in lines[i]:
            exists = True
            print(i + 1)
    if exists == False:
        print("Word does not exists")
    f.close()
except FileNotFoundError:
    print("File cannot be found")
except:
    print("Some error occurred")