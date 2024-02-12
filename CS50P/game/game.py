import random



level = input("Level: ")


if int(level) > 0:
    answer = random.randint(0, int(level))
    guess = input("Guess: ")
    print(answer)
    print(guess)
    if int(guess) == answer:
        print("correct")
    else:
        print("wrong")



