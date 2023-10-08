# TODO

height = int(input("Whats the height"))
while height > 8:
    height = input("Whats the height")
    width = int(height) - 1

for i in range(height):
    for j in range(width):
            print("#")