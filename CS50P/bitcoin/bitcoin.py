import requests
import json
import sys

while True:
    try:
        amount = sys.argv[1]
        try:
            r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
            bitcoin = r.json()
            price = bitcoin["bpi"]["USD"]["rate"]
            total = int(amount) * float(price)
            print(amount)
            print(price)
            print(total)
            break
        except requests.RequestException:
            sys.exit()
    except:
        print("please input correct arguments")
        break
