def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if len(s) < 2 or len(s) > 6:
        return False
    if s[0:2].isdigit() == True:
        return False
    if s.isalnum() == False:
        return False
    for i in range(len(s)):
        if s[i].isdigit() and s[i] == "0":
            

main()
