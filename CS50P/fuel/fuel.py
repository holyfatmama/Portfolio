
    try:
        xx = input("Fraction: ")
        x, y = xx.split("/")
        output = ((int(x) / int (y)) * 100)
        if output == 0:
            print("E")
        elif output == 100:
            print("F")
        else:
            print(f"{int(output)}%")
        break
    except:
        print("Error")
