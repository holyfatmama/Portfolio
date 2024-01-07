amount_due = 50
print(f"Amount Due: {amount_due}")

while amount_due > 0:
    x = int(input("Insert Coin:"))
    if (x % 25 == 0) or (x % 10 == 0) or (x % 5 == 0):
        amount_due = amount_due - x
    else:
        break
    if amount_due <= 0:
        print(f"Change Owed: {abs(amount_due)}")
    else:
        print(f"Amount Due: {amount_due}")



