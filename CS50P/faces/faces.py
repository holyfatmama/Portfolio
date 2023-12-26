def main():
    message = input()
    face = convert(message)
    print(face)
    return

def convert(x):
    y = x.replace(":)","🙂")
    y = x.replace(":(","🙁")
    return y

main()
