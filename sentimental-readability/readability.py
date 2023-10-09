# TODO
from cs50 import get_string

input = get_string("Text: ")

for i in range(len(input)):
    letters = str.isalpha(input[i-1])

print(letters)