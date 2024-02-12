import requests
import json
import sys

try:
    r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
    q = r.text
    w = json.loads(q)
    amount = w["bpi"]["USD"]["rate"]
    print("$" + amount)

except requests.RequestException:
    sys.exit()
