import random


while True:
    try:
        level = int(input("level: "))
        if level > 0:
            break
    except ValueError:
        print("please input an integer")

answer = random.randint(1, level)
guess = int(input("guess: "))

while True:
    if guess > answer:
        print("too large")
        guess = int(input("guess: "))
    if guess < answer:
        print("too little")
        guess = int(input("guess: "))
    else:
        print("correct!")
