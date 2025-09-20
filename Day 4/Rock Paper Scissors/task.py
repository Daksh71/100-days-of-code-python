import random




rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# Lists of choices and their matching ASCII art
image = [rock, paper, scissors]
yo1 = ["rock", "paper", "scissors"]

# Random choices
ran = random.randint(0, 2)
ran1 = random.randint(0, 2)

# Results
# result1 = yo1[ran]
result1=input("pls enter you choice rock , paper or scissors\n")
result2 = yo1[ran1]

# ✅ Print the name and the art
print(f"You chose: {result1}")
print(image[ran])

print(f"Computer chose: {result2}")
print(image[ran1])


if result1 == result2:
    print("It's a draw!")
elif (result1 == 0 and result2 == 2) or \
     (result1 == 1 and result2 == 0) or \
     (result1 == 2 and result2 == 1):
    print("You win!")
else:
    print("You lose!")