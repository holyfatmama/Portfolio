import requests
import json
import sys

#try:
r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
q = r.text
w = json.loads(q)
print(w)
#except requests.RequestException:

