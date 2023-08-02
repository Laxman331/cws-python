import os


def text_search(search_string, input_path_or_directory, output_file_path):
    if os.path.isfile(input_path_or_directory):
        f = open(input_path_or_directory, "r")
        content = f.readlines
        print(content)
    elif os.path.isdir(input_path_or_directory):
        pass
    else:
        print("It is not a file or directory")


text_search("aa", "abcd.txt", "y")
