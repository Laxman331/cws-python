"""Q4. Ask a string from user. Print the string with first 2 letters and
last 2 letters.
Example string: aeroplane
Output: aene"""

a = input("Enter a string = ")
print(a[0:2], end="")
print(a[-2::])
