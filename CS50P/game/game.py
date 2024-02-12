import random


while True:
    try:
        level = int(input("level: "))
        if level > 0:
            break
    except ValueError:
        print("please input an integer")

answer = random.randint(1, level)

while 
