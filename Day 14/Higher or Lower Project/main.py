from game_data import data
import random

print(f"Total entries: {len(data)}")

yo = input("does the user want to play the game? yes / no: ").lower()

if yo == "yes":
    score = 0
    while True:
        one = random.choice(data)
        two = random.choice(data)
        while two == one:
            two = random.choice(data)

        print("Compare the two:")
        print(f"One: {one['name']}, a {one['description']} from {one['country']} — ? million followers")
        print(f"Two: {two['name']}, a {two['description']} from {two['country']} — ? million followers")

        ans = input("Who has more followers? type 'one' or 'two': ").lower()

        counto = one['follower_count']
        countt = two['follower_count']

        if counto > countt:
            correct = "one"
        else:
            correct = "two"

        if ans == correct:
            print("correct!")
            score += 1
            print(f"Current score: {score}")
        else:
            print("wrong.")
            print(f"{correct} had more followers.")
            print(f"Final score: {score}")
            break
else:
    print("okay, maybe next time!")
