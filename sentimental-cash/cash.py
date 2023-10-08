# TODO
from cs50 import get_float
from cs50 import get_int

#get amount of cents from user

while True:
    cents = get_int("how many dollars")
    if cents > 0:
        break

# quarters
quarters = 0
while True:
    while (cents >= 25):
        cents = cents - 25
        quarters += 1
        break

print(quarters)

