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

human_player = int(input("Which do you choose? Type 0 for rock, 1 for paper, and 2 for scissors.\n"))
computer_player = random.randint(0,2)

# Attempt #1 - lots of ifs, no lists
# 0 beats 2
# 1 beats 0
# 2 beats 1
# 2 loses to 0
# 0 loses to 1
# 1 loses to 2

if human_player == 0 and computer_player == 2:
        print(rock)
        print("Computer chose:")
        print(scissors)
        print("You win!")
elif human_player == 1 and computer_player == 0:
        print(paper)
        print("Computer chose:")
        print(rock)
        print("You win!")
elif human_player == 2 and computer_player == 1:
        print(scissors)
        print("Computer chose:")
        print(paper)
        print("You win!")
elif human_player == 2 and computer_player == 0:
        print(scissors)
        print("Computer chose:")
        print(rock)
        print("You lose!")
elif human_player == 0 and computer_player == 1:
        print(rock)
        print("Computer chose:")
        print(paper)
        print("You lose!")
elif human_player == 1 and computer_player == 2:
        print(paper)
        print("Computer chose:")
        print(scissors)
        print("You lose!")
elif human_player == 1 and computer_player == 1:
        print(paper)
        print("Computer chose:")
        print(paper)
        print("Draw!")
elif human_player == 2 and computer_player == 2:
        print(scissors)
        print("Computer chose:")
        print(scissors)
        print("Draw!")
elif human_player == 0 and computer_player == 0:
        print(rock)
        print("Computer chose:")
        print(rock)
        print("It's a draw!")