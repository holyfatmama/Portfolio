# TODO
import cs50

height = get_int("height of tower")
while height > 8:
    width = int(height) - 1

for i in range(height):
    for j in range(width):
            print("#")