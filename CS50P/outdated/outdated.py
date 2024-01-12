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

if x[0].isnumeric:
    month, day, year = x.split("/")
    print(month, day, year)
elif x[0]:
    month, day, year = x.split("/")

month, day, year = x.split("/")
print(month, day, year)

if month not in months:
    print("error")
if int(day) > 31:
    print("error")

