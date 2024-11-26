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
import random
images = [rock, paper, scissors]

# Attempt 2 
# This version uses lists for the pictures and creates a simpler if/elif/else statements.

human_player = int(input("Which do you choose? Type 0 for rock, 1 for paper, and 2 for scissors.\n"))
if human_player == 0:
        print(images[0])
elif human_player == 1:
        print(images[1])
elif human_player == 2:
        print(images[2])
else:
        print("Invalid number.")


computer_player = random.randint(0,2)
print(f"Computer chose:")
if computer_player == 0:
        print(images[0])
elif computer_player == 1:
        print(images[1])
elif computer_player == 2:
        print(images[2])

# 0 beats 2
# 1 beats 0
# 2 beats 1
# 2 loses to 0
# 0 loses to 1
# 1 loses to 2

if human_player == 0 and computer_player == 2:
        print("You win!")
elif human_player == 1 and computer_player == 0:
        print("You win!")
elif human_player == 2 and computer_player == 1:
        print("You win!")
elif human_player == 2 and computer_player == 0:
        print("You lose!")
elif human_player == 0 and computer_player == 1:
        print("You lose!")
elif human_player == 1 and computer_player == 2:
        print("You lose!")
elif human_player == 1 and computer_player == 1:
        print("It's a draw!")
elif human_player == 2 and computer_player == 2:
        print("It's a draw!")
elif human_player == 0 and computer_player == 0:
        print("It's a draw!")
