# TODO
from cs50 import get_string

input = get_string("Text: ")

letters = 0
for i in range(len(input)):
    if (str.isalpha(input[i]) == True):
        letters += 1
    elif (str.isspace(input[i]) == True):
        letters - 1

print(f"Letters: {letters}")

words = 1
for i in range(len(input)):
    if (str.isspace(input[i]) == True):
        words += 1

print(f"Words: {words}")

sentences = 0
for i in range(len(input)):
    if 
