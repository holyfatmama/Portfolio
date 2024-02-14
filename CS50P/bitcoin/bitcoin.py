import requests
import json
import sys


while True:
    try:
        if len(sys.argv) != 2:
            print("Missing command-line argument")
            sys.exit(1)
        else:
            try:
                number = float(sys.argv[1])
                r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
                data = r.json()
                price = data["bpi"]["USD"]["rate_float"]
                amount = number * price
                print(f"${amount:,.4f}")
                sys.exit(0)
            except ValueError:
                print("Command-line argument is not a number")
                sys.exit(1)
    except requests.RequestException:
        sys.exit(1)

