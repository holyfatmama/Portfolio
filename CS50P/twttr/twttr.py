x = input("Input:")

for i in x:
    if i.lower() == "a" or i.lower() == "e" or i.lower() == "i" or i.lower() == "o" or i.lower() == "u":
        print("", end = "")
    else:
        print(i, end = "")

print()
