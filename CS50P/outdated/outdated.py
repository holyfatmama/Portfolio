x = input("Date: ")

month, day, year = x.split("/", "")
print(month, day, year)

if int(month) > 12:
    print("error")
if int(day) > 31:
    print("error")

