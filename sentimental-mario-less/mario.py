# TODO
from cs50 import get_int

height = get_int("height of tower?")

while true:
      height = get_int("height of tower?")
      if height > 8 or < 1:
            break
      return height

width = height - 1

for i in range(height):
    print("#", end="")
