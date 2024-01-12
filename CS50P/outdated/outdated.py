months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]

x = input("Date: ")

month, day, year = x.split("/", "")
print(month, day, year)

if int(month) > 12 or month not in months:
    print("error")
if int(day) > 31:
    print("error")

