def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() == False:
        return False
    if len(s) < 2 and len(s) > 6:
        return False
    if i[-1].isalpha() == True:
        return False
    

main()
