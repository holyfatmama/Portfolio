def main():
    y = input()
    convert(y)
    print(y)

def convert(x):
    x = x.replace(":)","🙂")
    x = x.replace(":(","🙁")
    return x

main()
