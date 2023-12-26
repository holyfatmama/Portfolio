def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    # TODO
    e = float(d.replace("$",""))
    return e


def percent_to_float(p):
    # TODO
    q = (float(p.replace("%","")))/100
    return q


main()
