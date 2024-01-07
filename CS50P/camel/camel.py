x = input("camelCase:")

for i in x:
    if i.isupper():
        print("_" + i, end = "")
    else:
        print(i, end = "")

print()
