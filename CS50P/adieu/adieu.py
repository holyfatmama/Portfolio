import inflect

p = inflect.engine()

names = []
while True:
    try:
        name = input("Name: ")
        names.appened(name)
    except EOFError:
        print("Adieu, Adieu, to", )

