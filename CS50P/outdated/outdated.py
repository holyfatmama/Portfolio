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
        month, day, year = date2.split()
        if month in months:
            print(months.index(month) + 1)
            print(f"{year}/{day:.02}/{month}")
    except:
        print("error2")
