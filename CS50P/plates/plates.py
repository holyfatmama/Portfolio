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
    if s[-1].isnumeric == True:
        return False
    for i in s:
        if i.isalnum() == False:
            if i == '0':
                return False
    for c in s:
        if c.isalnum() == False:
            return False
    return True

main()
