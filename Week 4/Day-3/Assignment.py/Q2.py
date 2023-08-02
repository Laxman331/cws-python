"""Q2. Write a Python program to check if a dictionary is empty or not."""
a = {}
count = 0
for i in a:
    count = count + 1
if count >= 1:
    print("not empty")
else:
    print("empty")
