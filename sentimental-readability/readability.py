# TODO
from cs50 import get_string

input = get_string("Text: ")

letters = 0
for i in range(len(input)):
    if str.isalpha(input[i]) == True:
        letters += 1
    elif str.isspace(input[i]) == True:
        letters - 1

print(f"Letters: {letters}")

words = 1
for i in range(len(input)):
    if str.isspace(input[i]) == True:
        words += 1

print(f"Words: {words}")

sentences = 0
for i in range(len(input)):
    if input[i] == "." or input[i] == "?" or input[i] == "!":
        sentences += 1

print(f"Sentences: {sentences}")

L = letters / words * 100
S = sentences / words * 100

index = round(0.0588 * L - 0.296 * S - 15.8)

if index < 1:
    print("Before Grade 1")
elif index > 16:
    print("Grade 16+")
else:
    print(f"Grade: {index}")

print(input.count("."))