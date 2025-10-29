import random

rock = ("""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
""")

paper = ("""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
""")

scissors = ("""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
""")

game_images = [rock, paper, scissors]
print ("Welcome to Rock, Paper, Scissors:")
user_choice = int(input("0 for rock, 1 for paper, 2 for scissors: "))
if user_choice >=0 and user_choice <=2:
    print(game_images[user_choice])
computer_choice = random.randint(0, 2)
print(f"Computer chose:")
print(game_images[computer_choice])

if user_choice == 0 and computer_choice == 2:
    print ("You Win!")
elif computer_choice == 0 and user_choice == 2:
    print ("You Lose!")
elif computer_choice > user_choice:
    print ("You Lose!")
elif user_choice > computer_choice:
    print ("You Win!")
elif computer_choice == user_choice:
    print("It's a Draw!")


