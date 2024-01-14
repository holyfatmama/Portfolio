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

x = input("1:")

try:
    if x[0].isnumeric:
        month, day, year = x.split("/")
        print(month, day, year)
except:
    print("error")

if x[0].isdigit == False:
    x = x.strip(",")
    month = x.split()
    print(month)
