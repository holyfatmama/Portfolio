import random



level = input("Level: ")


if int(level) > 0:
    answer = random.randint(0, level)
    guess = input("Guess: ")
    if guess == answer:
        print("correct")
    else:
        print("wrong")



