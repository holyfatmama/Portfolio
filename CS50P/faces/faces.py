def main():
    message = input()
    face = convert(message)
    print(face)

def convert(x):
    y = x.replace(":)","🙂")
    z = y.replace(":(","🙁")
    return z

main()
