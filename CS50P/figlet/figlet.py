from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

text = input("Input:")

if len(sys.argv) == 1 or len(sys.argv) == 3:
    if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        f = sys.argv[2]
        figlet.setFont(font=f)
        print(figlet.renderText(text))
    else:
        list = figlet.getFonts()
        f = random.choice(list)
        figlet.setFont(font=f)
        print(figlet.renderText(text))
else:
    sys.exit
