amount_due = 50
print(f"Amount Due: {amount_due}")

while amount_due > 0:
    x = int(input("Insert Coin:"))
    if (x == 25) or (x == 10) or (x == 5):
        amount_due = amount_due - x
    if amount_due <= 0:
        print(f"Change Owed: {abs(amount_due)}")
    else:
        print(f"Amount Due: {amount_due}")



