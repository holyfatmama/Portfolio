def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s[0:2].isalpha() == False:
        return False
    if len(s) < 2 or len(s) > 6:
        return False
    for i in range(len(s)):
        if s[i].isdigit() == True:
            if int(s[i]) == 0:
                return False
        else:
            break
    for i in range(len(s)-1):
        if s[i].isdigit() == True and s[i+1].isalpha() == True:
            return False
    if s.isalnum() == False:
        return False
    return True

main()
