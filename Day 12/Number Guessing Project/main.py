import random

def selected():
    numbers = list(range(1, 101))
    sel1 = random.choice(numbers)
    return sel1

level = input("Pls choose the level you want to work on easy or hard ").lower()

rand = selected()
print(rand)

if level == "easy":
    print("User gets 10 attempts to try to guess the number")
    attempt = 10

    for i in range(attempt):
        guess = int(input("Pls enter your number: "))

        if guess == rand:
            print("You have guessed the right answer!")
            break
        else:
            attempt -= 1
            print(f"Wrong guess. Attempts left: {attempt}")

    if attempt == 0:
        print(f"You ran out of attempts. The number was {rand}.")

elif level == "hard":
    print("User gets 5 attempts to try to guess the number")
    attempt = 5

    for i in range(attempt):
        guess = int(input("Pls enter your number: "))

        if guess == rand:
            print(" You have guessed the right answer!")
            break
        else:
            attempt -= 1
            print(f"Wrong guess. Attempts left: {attempt}")

    if attempt == 0:
        print(f"You ran out of attempts. The number was {rand}.")
