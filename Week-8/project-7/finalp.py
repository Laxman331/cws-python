import os
import re


def text_search(search_string, input_path, output_file_path):
    # Open the output file for writing the results
    output_file = open(output_file_path, "w")

    # Check if the input path is a file or a directory
    if os.path.isfile(input_path):
        # If it's a file, search the text string in that file
        with open(input_path, "r") as input_file:
            file_contents = input_file.read()
        search_in_file(search_string, input_path, file_contents, output_file)
    elif os.path.isdir(input_path):
        # If it's a directory, search the text string in all text files within the directory and its subdirectories
        for root, _, files in os.walk(input_path):
            for file_name in files:
                file_path = os.path.join(root, file_name)

                # Check if the file is a text file
                if file_path.lower().endswith(".txt"):
                    with open(file_path, "r") as input_file:
                        file_contents = input_file.read()
                    search_in_file(search_string, file_path, file_contents, output_file)
    else:
        print("Invalid input. Please provide a valid file or directory path.")

    output_file.close()


def search_in_file(search_string, file_name, file_contents, output_file):
    search_string_lower = search_string.lower()
    file_contents_lower = file_contents.lower()

    # Split the file contents into lines
    lines = file_contents_lower.split("\n")

    # Iterate through the lines to find the search_string using re.search()
    for line_number, line in enumerate(lines, 1):
        if re.search(search_string_lower, line):
            output_file.write(f"{file_name}:{line_number}\n")


search_string = "hello"
input_path = "c:\A3-PYPRO\Week-8\project-7\finalp.py"  # Replace with the correct path to the file or directory
# make sure to use raw string for entering path
output_file_path = "results.txt"
text_search(search_string, input_path, output_file_path)
