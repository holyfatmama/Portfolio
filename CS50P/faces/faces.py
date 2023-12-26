def main():
    y = input()
    convert(y)
    print(y)

def convert(x):
    x.replace(":)","🙂")
    x.replace(":(","🙁")
    return x

main()
