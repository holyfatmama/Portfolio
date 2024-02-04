from pyfiglet import Figlet
import sys


figlet = Figlet()
x = input("heheL")

if len(sys.argv) == 1 or 3:
    if sys.argv[1] != "-f":
        print("Invalid Usage")
        exit()
    else:
        figlet.setFont(font = sys.argv[2])
        print(figlet.renderText(x))
else:
    exit()
