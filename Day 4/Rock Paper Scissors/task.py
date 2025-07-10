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
game_image = [rock,paper,scissors]
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
if user_choice >=0 or user_choice > 3:
    print(game_image[user_choice])
#0, 1, 2
computer_choice = random.randint(0,2)
print("Computer Choose")
print(game_image[computer_choice])

#conditions
if user_choice >= 3 or user_choice <0:
    print("You entered Invalid Number. You lose")
elif user_choice == 0 and computer_choice == 2:
    print("you Win!")
elif user_choice == 2 and computer_choice == 0:
    print("You lose!")
elif user_choice ==1 and computer_choice ==2:
    print("You win!")
elif computer_choice > user_choice:
    print("You Lose!")
elif user_choice > computer_choice:
    print("You Win!")
elif computer_choice == user_choice:
    print("It's Draw!")

