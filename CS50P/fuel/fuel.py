while True:
    try:
        xx = input("Fraction: ")
        x, y = xx.split("/")
        output = int(x) / int (y)
        percentage = output * 100
        if 0 <= output <= 1:
            print("E")
            break
        elif 99 <= output <= 100:
            print("F")
            break
        else:
            print(f"{int(output)}%")
            break
    except:
        print("Error")
