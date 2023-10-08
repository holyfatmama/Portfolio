# TODO
from cs50 import get_int

# get height of tower from user
while True:
      n = get_int("height of tower?")
      if n > 0 and n < 9:
            break

#print height
for i in range(1, n + 1):
      print("" * )