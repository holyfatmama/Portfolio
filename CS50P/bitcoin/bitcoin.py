import requests
import json
import sys

while True:
    try:
        amount = sys.argv[1]
        try:
            r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            w = r.json()
            amount = w["bpi"]["USD"]["rate"]
            print(w)
            break
        except requests.RequestException:
            sys.exit()
    except:
        print("please input correct arguments")
