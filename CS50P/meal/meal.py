def main():
    time = input("What time is it? ")
    answer = convert(time)
    print
    if hours >= 7 and hours <= 8:
        print("breakfast time")
    elif hours >= 12 and hours <=13:
        print("lunch time")
    elif hours >= 18 and hours <= 19:
        print("dinner time")

def convert(time):
    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)
    minutes = minutes / 60
    return hours, minutes

if __name__ == "__main__":
    main()
