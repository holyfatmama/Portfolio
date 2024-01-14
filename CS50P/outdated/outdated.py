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

x = input("date:")

try:
    month, day, year = date.split("/")
    if (1 <= month <= 12) and (1 <= day <= 31):
        print(year, month, da)
except:
    try:
        date = date.strip(",")
        month, day, year = date.split()
        print(month)
    except:
        print("error")
