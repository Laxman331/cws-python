"""Q3. Write a Python program that takes a user's input for a file
name and tries to read the content of the file. If the file does not
exist, print an error message using exception handling.
Example input: nonexistent_file.txt
Example output: Error: File not found."""
try:
    file_name = input("Enter file name =")
    f = open(mode="r", file=file_name)
    a = f.read()
    print(a)
except:
    print("Error: File not found.")
