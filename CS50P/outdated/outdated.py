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

date = input("date:")

try:
    month, day, year = date.split("/")
    if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
        print(year, month, day)
    else:
        print("error1")
except:
    try:
        date2 = date.replace("," , "")
        print(date2)
        month, day, year = date2.split()
        if month in months:
            print(f"{year}/{day}/{months.index(month) + 1}")
    except:
        print("error2")
