"""
Ask sentence
Ask letter


If letter exists
    Then only ask new letter
    Then replace old letter with new letter

Else
    Print does not exists
"""


a = input("Enter a sentence = ")
b = input("Enter a letter = ")
if a.find(b) != -1:
    c = input("Enter new letter = ")
    result = a.replace(b, c)
    print(result)
else:
    print("Letter does not exist")
