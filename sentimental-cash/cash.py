# TODO
from cs50 import get_int

#get amount of cents from user

cents = get_int("how many cents")

# quarters
quarters = 0
while (cents >= 25):
    cents = cents - 25
    quarters += 1

