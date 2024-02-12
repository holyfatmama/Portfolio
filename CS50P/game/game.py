import random



while True:
    try:
        level = input("Level: ")
        if level > 0:
            answer = random.randint(1, level)
            guess = input("Guess: ")
            break
    except:
        print("input an integer")


