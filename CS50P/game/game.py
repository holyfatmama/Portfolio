import random



while True:
    try:
        level = input("Level: ")
        if int(level) > 0:
            answer = random.randint(1, level)
            guess = input("Guess: ")
            if guess == answer:
                print("correct")
            else:
                print("wrong")
            break
    except:
        print("input an integer")
        break

