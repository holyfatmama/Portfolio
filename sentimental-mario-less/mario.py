# TODO
from cs50 import get_int

height = get_int("height of tower?")

width = height - 1

for i in range(height):
    for j in range(width):
            print("#")
