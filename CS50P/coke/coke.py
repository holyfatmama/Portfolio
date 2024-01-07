amount_due = 50
print(f"Amount Due: {amount_due}")

x = int(input("Insert Coin:"))

amount_due = amount_due - x
while amount_due > 0:
    x = int(input("Insert Coin:"))
    amount_due - x
print(amount_due)
