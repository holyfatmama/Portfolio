def main():
    y = str(input())
    convert(y)
    print(y)

def convert(x):
    x.replace(":)","🙂")
    x.replace(":(","🙁")
    return x

main()
