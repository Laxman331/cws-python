import os
import re


def text_search(search_string, input_path, output_file):
    with open(output_file, "w") as result_file:
        if os.path.isfile(input_path):
            search_in_file(search_string, input_path, result_file)
        elif os.path.isdir(input_path):
            for root, _, files in os.walk(input_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    search_in_file(search_string, file_path, result_file)


def search_in_file(search_string, file_path, result_file):
    with open(file_path, "r") as file:
        line_number = 0
        for line in file:
            line_number += 1
            if re.search(search_string, line):
                result_file.write(f"{file_path}:{line_number}: {line.strip()}\n")


# if __name__ == "__main__":
#     search_string = "hello"
#     input_path = "myfiles"
#     output_file = "results.txt"

#     text_search(search_string, input_path, output_file)
text_search("hello", "project-7", "results.txt")
