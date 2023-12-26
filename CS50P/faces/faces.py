def main():
    message = input()
    face = convert(message)
    print(face)

def convert(x):
    y = x.replace(":)","🙂").replace(":(","🙁")
    return y

main()
