def main():
    time = input("What time is it? ")
    answer = convert(time)
    print(answer)
    
def convert(time):
    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)
    minutes = minutes / 60
    return hours + minutes

if __name__ == "__main__":
    main()
