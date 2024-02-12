import requests
import json
import sys

while True:
    try:
        r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        w = r.json()

        amount = w["bpi"]["USD"]["rate"]
        amount = float(amount)
        print(amount)
        break

    except requests.RequestException:
        sys.exit()
