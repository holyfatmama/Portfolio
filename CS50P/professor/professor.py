import random


def main():
    get_level()
    generate_integer(1)


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
        print(f"{x} + {y}:", end=" ")
        answer = int(input(""))
        answer_count = 0
        if answer == z and answer_count < 3:
            count +=1
        else:
            answer_count += 1
            print("eee")
    print(f"Score: {count}")



if __name__ == "__main__":
    main()
