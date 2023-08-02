"""Q1. Make a text file. Enter random numbers in that file. Each line
must contain only one number. Write a python program to
calculate the sum of all the numbers."""
f = open("abcd.txt", "r")
a = f.readlines()
lines = list(map(int, a))
print(sum(lines))
