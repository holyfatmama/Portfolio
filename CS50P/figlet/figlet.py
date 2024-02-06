from pyfiglet import Figlet
import sys


figlet = Figlet()

text = input("heheL")

if len(sys.argv) == 1 or len(sys.argv) == 3:
    if len(sys.argv) == 3:
        f = sys.argv[2]
        figlet.setFont(font=f)
        print(figlet.renderText(text))
