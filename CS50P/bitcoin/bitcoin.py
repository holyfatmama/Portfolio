import requests
import json
import sys

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    w = r.text.json

    amount = float(w["bpi"]["USD"]["rate"])

    print(amount)

except requests.RequestException:
    sys.exit()
