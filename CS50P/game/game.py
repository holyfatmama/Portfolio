import random


while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
        else:
            print("please input positive integer")
    except ValueError:
        print("please input an integer")

answer = random.randint(1, level)
guess = int(input("Guess: "))

while True:
    if guess > answer:
        print("Too Large!")
        guess = int(input("Guess: "))
    if guess < answer:
        print("Too Small!")
        guess = int(input("Guess: "))
    else:
        print("Just Right!")
        break
