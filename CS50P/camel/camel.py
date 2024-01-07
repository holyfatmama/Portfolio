x = input("camelCase:")

for i in x:
    if i.isupper():
        print("_" + i.lower(), end = "")
    else:
        print(i, end = "")

print()
