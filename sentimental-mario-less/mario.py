# TODO
from cs50 import get_int

# get height of tower from user
while True:
      height = get_int("height of tower?")
      if height > 0 & height < 9:
            break

#print height 
h = 0
while h < height:
      print("#")
      h += 1
