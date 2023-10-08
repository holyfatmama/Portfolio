# TODO
from cs50 import get_int

# get height of tower from user
while True:
      height = get_int("height of tower?")
      if height < 1 or height > 8:
            break

#print height
