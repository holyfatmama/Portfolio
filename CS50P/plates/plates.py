def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha():
    if len(s) >= 2 and len(s) <= 6:
        return
    else:
        return False


main()
