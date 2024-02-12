import random


def main():
    ...


def get_level():
    level = int(input("Level: "))
    while True:
        try:
            if 1 <= level <= 3:
                return level
        except ValueError:
            print("input an integer between 1 and 3")


def generate_integer(level):
    ...


if __name__ == "__main__":
    main()
