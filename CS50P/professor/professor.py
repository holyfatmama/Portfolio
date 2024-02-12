import random


def main():
    generate_integer(get_level())


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if 1 <= level <= 3:
                return level
        except ValueError:
            print("input an integer between 1 and 3")


def generate_integer(level):
    number = 10
    count = 0
    for i in range(number):
        x = random.randint(1, 10)
        y = random.randint(1, 10)
        z = x + y
        for i in range(3):
            print(f"{x} + {y}:", end=" ")
            try:
                answer = int(input(""))
            except ValueError:
                print("please input integer:")
                answer = int(input(""))
            if answer == z:
                count +=1
                print("correct")
                break
            else:
                print("eee")

    print(f"Score: {count}")


if __name__ == "__main__":
    main()
