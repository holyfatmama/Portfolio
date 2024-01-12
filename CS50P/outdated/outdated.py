x = input("Date: ")

month, day, year = x.split()
print(month, day, year)

if month > 12:
    print("error")
if day > 31:
    print("error")

