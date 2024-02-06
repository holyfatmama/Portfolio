from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


if len(sys.argv) == 1 or len(sys.argv) == 3:
    if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        text = input("Input:")
        f = sys.argv[2]
        figlet.setFont(font=f)
        print(f"Output:{figlet.renderText(text)}")
    else:
        text = input("Input:")
        list = figlet.getFonts()
        f = random.choice(list)
        figlet.setFont(font=f)
        print(f"Output:{figlet.renderText(text)}")
else:
    sys.exit
    print("Invalid usage")
