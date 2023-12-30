x = input("What is the Answer to the Great Question of Life, the Universe, and Everything?")

answer = x.strip().lower()

if answer == "forty-two" or "forty two" or "42":
    print("Yes")
else:
    print("No")
