prices = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total_price = 0
while True:
    try:
        item = input("Item: ").title()
        if item in prices:
            total_price = total_price + float(prices[item])
    except EOFError:
        total_price = round(total_price, 2)
        print(f"${total_price}")


