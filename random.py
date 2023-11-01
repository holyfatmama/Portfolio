stock = [{"name": "jun"}, {"name": "han"}]

stock2 = {}
stock2["name"] = stock[0]["name"]
print(stock2["name"])
print(stock2)

for sto in stock:
    print(sto)

shares = [{"symbol" : "aapl", "SUM(shares)" : 4}, {"symbol" : "tsla", "SUM(shares)" : 6}]
share = {"gay":"yes"}
share["values"] = shares[0]["SUM(shares)"] + shares[1]["SUM(shares)"]
print(share)


