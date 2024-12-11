logo = '''   
   ____                       _____ _            _   _                 _               _ 
  / ___|_   _  ___  ___ ___  |_   _| |__   ___  | \ | |_   _ _ __ ___ | |__   ___ _ __| |
 | |  _| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ |  \| | | | | '_ ` _ \| '_ \ / _ \ '__| |
 | |_| | |_| |  __/\__ \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |  |_|
  \____|\__,_|\___||___/___/   |_| |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  (_)
  '''

import random

EASY_ATTEMPTS = 10
HARD_ATTEMPTS = 5

def check_ans(guess, number_answer, turns):
    if guess < number_answer:
        print(f"Your guess is too low.")
        return turns - 1
    elif guess > number_answer:
        print(f"Your guess is too high.")
        return turns - 1
    elif guess == number_answer:
        print(f"You win! The number is {number_answer}!")


def check_diff():
    difficulty = input("Choose a difficulty. Type \"easy\" or \"hard\"\n").lower()
    if difficulty == "easy":
        return EASY_ATTEMPTS
    else:
        return HARD_ATTEMPTS


def game():
    print(logo)
    print("Welcome to Guess the Number!")
    print("I'm thinking of a number between 1 and 100.")
    number_answer = random.choice(range(1, 101))

    turns = check_diff()
    guess = 0

    while guess != number_answer:
        print(f"Attempts remaining = {turns}")
        guess = int(input("What is your guess?\n"))
        turns = check_ans(guess, number_answer, turns)
        if turns == 0:
            return input(f"No attempts remaining. The number was {number_answer}.")
        elif guess != number_answer:
            print("Try again.")

game()