# TODO
from cs50 import get_int


while True:
      height = get_int("height of tower?")
      if height > 0 & height < 9:
            break

width = height - 1

for i in range(height):
    print("#", end="")
