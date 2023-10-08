# TODO
from cs50 import get_float

# get amount of cents from user
while True:
    dollars = get_float("how many dollars\n")
    if dollars > 0:
        break

# convert dollars to cents and round it to an integer to ensure precision
cents = round(dollars * 100)

# quarters
quarters = 0
while cents >= 25:
    cents = cents - 25
    quarters += 1

# dime
dime = 0
while cents >= 10:
    cents = cents - 10
    dime += 1


# nickel
nickel = 0
while cents >= 5:
    cents = cents - 5
    nickel += 1

# pennies
pennies = 0

while cents >= 1:
    cents = cents - 1
    pennies += 1

coins = quarters + dime + nickel + pennies

print(coins)
