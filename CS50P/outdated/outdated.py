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



while True:
        date = input("date:")
        try:
            month, day, year = date.split("/")
            if (1 <= int(month) <= 12) and (1 <= int(day) <= 31):
                break
        except:
            try:
                
                date2 = date.replace("," , "")
                month, day, year = date2.split()
                if month in months and 1 <= int(day) <= 31:
                    month = (months.index(month) + 1)
                    break
            except:
                 print("hehexd")


print(f"{int(year):02}-{int(month):02}-{int(day):02}")
