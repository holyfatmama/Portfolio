import requests
import json
import sys


while True:
    try:
        if len(sys.argv) != 2:
            print("please input correct amount of arguments")
            sys.exit()
        else:
            try:
                amount = float(sys.argv[1])
                print("okay")
                break
            except ValueError:
                print("please input correct arguments")
                sys.exit()
    except requests.RequestException:
        sys.exit()

