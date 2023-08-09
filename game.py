import random

while True:
    try:
        level = input("Level: ")

        n = int(level)

        if n > 0:
            num = random.randint(1, n)
            break

    except ValueError:
        pass

while True:
    try:
        guess = input("Guess: ")

        if int(guess) > 0:
            if int(guess) > num:
                print("Too Large!")

            if int(guess) < num:
                print("Too Small!")

            if int(guess) == num:
                print("Just Right!")
                break

    except ValueError:
        pass




