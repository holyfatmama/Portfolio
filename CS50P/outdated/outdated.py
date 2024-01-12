x = input("Date: ")

month, day, year = x.split()

if month > 12:
    print("error")
if day > 31:
    print("error")

