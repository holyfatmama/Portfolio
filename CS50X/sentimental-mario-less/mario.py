# TODO
from cs50 import get_int

# get height of tower from user
while True:
      height = get_int("Height: ")
      if height > 0 and height < 9:
            break

#print height
for i in range(1, height + 1):
      print(" " * (height - i) + "#" * i)