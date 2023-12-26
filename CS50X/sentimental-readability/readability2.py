from cs50 import get_string

#input
input = get_string("Text:")

letters = 0
for i in input:
    if i.isalpha():
        letters += 1
print(letters)

words = input.count(" ") + 1
print(words)

sentences = input.count("!") + input.count ("?") + input.count (".")
print(sentences)

L = letters / words * 100
S = sentences / words * 100

index = round(0.0588 * L - 0.296 * S - 15.8)
print(index)

if index <1:
    print("before grade 1")
elif index >16:
    print