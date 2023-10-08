# TODO
from cs50 import get_float

#get amount of cents from user

while True:
    dollars = get_float("how many dollars\n")
    if dollars > 0:
        break

# quarters
quarters = 0

while (dollars >= 0.25):
        dollars = dollars - 0.25
        quarters += 1

# dime
dime = 0
while (dollars >= 0.10):
     dollars = dollars - 0.10
     dime += 1


# nickel
nickel = 0

while (dollars >= 0.05):
     dollars = dollars - 0.05
     nickel += 1

# pennies
pennies = 0

while (dollars >= 0.01):
     dollars = dollars - 0.01
     pennies += 1

coins = quarters + dime + nickel + pennies


print(coins)


