from pyfiglet import Figlet
import sys
import random

figlet = Figlet()


if len(sys.argv) == 1 or len(sys.argv) == 3:
    if len(sys.argv) == 3 and (sys.argv[1] == "-f" or sys.argv[1] == "--font"):
        f = sys.argv[2]
        list = figlet.getFonts()
        if f in list:
            text = input("Input:")
            figlet.setFont(font=f)
            print(f"Output:{figlet.renderText(text)}")
        else:
            sys.exit
            print("Invalid usage")
    elif len(sys.argv) == 1:
        text = input("Input:")
        list = figlet.getFonts()
        f = random.choice(list)
        figlet.setFont(font=f)
        print(f"Output:{figlet.renderText(text)}")
    else:
        sys.exit
        print("Invalid usage")
else:
    sys.exit
    print("Invalid usage")
