# TODO
from cs50 import get_string

input = get_string("Text: ")

letters = 0
for i in range(len(input)):
    if (str.isalpha(input[i-1]) == True):
        letters += 1
    elif (str.isspace(input[i-1]) == True):
        letters - 1

print(letters)

words = str.count(input)
print(words)