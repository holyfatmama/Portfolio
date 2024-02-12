import random


while True:
    try:
        level = int(input("Level: "))
        if level > 0:
            break
        else:
            print("please input positive integer")
            level = int(input("Level: "))
    except ValueError:
        print("please input an integer")

answer = random.randint(1, level)
guess = int(input("guess: "))

while True:
    if guess > answer:
        print("Too Large")
        guess = int(input("guess: "))
    if guess < answer:
        print("Too Small!")
        guess = int(input("guess: "))
    else:
        print("Correct!")
        break
