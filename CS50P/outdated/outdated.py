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

if x[0].isdigit:
    month, day, year = x.split("/")
    print(month, day, year)

if x[0].isalpha:
    
