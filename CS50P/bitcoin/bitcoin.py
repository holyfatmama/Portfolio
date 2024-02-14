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
                amount = float(sys.argv[1])
                r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")

                print(r)
                break
            except ValueError:
                print("Command-line argument is not a number")
                sys.exit(1)
    except requests.RequestException:
        sys.exit(1)

