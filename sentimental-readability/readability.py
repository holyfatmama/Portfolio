# TODO
from cs50 import get_string

input = get_string("Text: ")

letters = len(input)

words = str.count(input)
print(words)