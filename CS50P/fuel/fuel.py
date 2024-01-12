while True:
    try:
        xx = input("Fraction: ")
        x, y = xx.split("/")
        output = int(x) / int (y)
        percentage = output * 100
        if 0 <= percentage <= 100:
            try:
                if 0 <= percentage <= 1:
                    print("E")
                    break
                elif 99 <= percentage <= 100:
                    print("F")
                    break
                else:
                    print(f"{int(percentage)}%")
                    break
            except:
                print("error")
    except:
        print("Error")
