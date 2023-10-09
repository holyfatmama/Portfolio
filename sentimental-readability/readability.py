# TODO
from cs50 import get_string

input = get_string("Text: ")

letters = 0
for i in range(len(input)):
    letter = str.isalpha(input[i-1])
    letters += 1

print(letters)