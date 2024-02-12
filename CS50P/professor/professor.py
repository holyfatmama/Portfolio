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
    count = 0
    difficulty = [9, 99, 999]
    difficulty_start = [0, 10, 100]
    for i in range(10):
        x = random.randint(difficulty_start[level - 1], difficulty[level - 1])
        y = random.randint(difficulty_start[level - 1], difficulty[level - 1])
        z = x + y
        for i in range(3):
            print(f"{x} + {y}:", end=" ")
            try:
                answer = int(input(""))
                if answer == z:
                    count +=1
                    print("correct")
                    break
                else:
                    print("EEE")
            except ValueError:
                print("EEE")


    print(f"Score: {count}")


if __name__ == "__main__":
    main()
