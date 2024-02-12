import random


def main():
    get_level()
    generate_integer(1)


def get_level():
    level = int(input("Level: "))
    while True:
        try:
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
        print(f"{x} + {y}:", end=" ")
        answer = int(input(""))
        answer_count = 0
        while answer_count < 3:
            answer = int(input(""))
            if answer == z:
                count += 1
                continue
            else:
                print("EEE")
                answer_count += 1



if __name__ == "__main__":
    main()
