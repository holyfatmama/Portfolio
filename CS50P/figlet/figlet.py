from pyfiglet import Figlet
import sys


figlet = Figlet()
x = input("heheL")

if len(sys.argv) == 1 or len(sys.argv) == 3:
    font = sys.argv[1]
    
