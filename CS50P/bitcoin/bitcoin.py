import requests

#try:
r = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
print(r)
#except requests.RequestException:

