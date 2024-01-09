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
    for i in s:
        if i.isalpha == False and i == '0':
            break
        return False
    for i in range(len(s)-1):
        if s[i].isnumeric() == True and s[i+1].isalpha() == True:
            return False
    for c in s:
        if c.isalnum() == False:
            return False
    return True

main()
