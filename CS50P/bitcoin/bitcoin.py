import requests
import json
import sys

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    q = r.text
    w = json.loads(q)
    x = w["bpi"]["USD"]["rate"]
    amount = float(x)
    print(amount)

except requests.RequestException:
    sys.exit()
