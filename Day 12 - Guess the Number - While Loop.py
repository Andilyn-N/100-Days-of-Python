logo = '''   
   ____                       _____ _            _   _                 _               _ 
  / ___|_   _  ___  ___ ___  |_   _| |__   ___  | \ | |_   _ _ __ ___ | |__   ___ _ __| |
 | |  _| | | |/ _ \/ __/ __|   | | | '_ \ / _ \ |  \| | | | | '_ ` _ \| '_ \ / _ \ '__| |
 | |_| | |_| |  __/\__ \__ \   | | | | | |  __/ | |\  | |_| | | | | | | |_) |  __/ |  |_|
  \____|\__,_|\___||___/___/   |_| |_| |_|\___| |_| \_|\__,_|_| |_| |_|_.__/ \___|_|  (_)
  '''

import random
print(logo)
print("Welcome to Guess the Number!")

difficulty = input(
    "I'm thinking of a number between 1 and 100."
    "\nChoose a difficulty. Type \"easy\" or \"hard\"\n").lower()

number_answer = random.choice(range(1, 101))
# print(number_answer)

attempts = ""
if difficulty == "easy":
    attempts = 10
else:
    attempts = 5

# print(attempts)
print(f"Attempts remaining = {attempts}")
guessing_seq = True

while guessing_seq:
    if attempts == 0:
        print(f"No attempts remaining. The number was {number_answer}.")
        guessing_seq = False
    else:
        guess = int(input("Make a guess:  "))
        if guess < number_answer:
            print("Your guess is too low.")
            attempts -= 1
            print(f"Attempts remaining = {attempts}")
        elif guess > number_answer:
            print("Your guess is too high.")
            attempts -= 1
            print(f"Attempts remaining = {attempts}")
        elif guess == number_answer:
            print(f"You win! The number is {number_answer}!")
            guessing_seq = False