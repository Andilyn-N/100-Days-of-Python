from game_data import data
from art import vs
from art import logo
import random

# print(logo)

def data_values(account):
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description} from {country}"

keys = list(data)
choice_A = random.choice(keys)

print(f"Compare A: {data_values(choice_A)}")

# print(vs)

choice_B = random.choice(keys)

print(f"Against B: {data_values(choice_B)}")

def game():
    score = 0
    game_continue = True
    while game_continue is True:
        player_guess = input("Who has more Instagram followers? Type \"A\" or \"B\":  ").upper()
        if choice_A > choice_B and player_guess == "A":
            score += 1
            print(f"That's right. Your score is {score}.")
            switch()
        elif choice_A < choice_B and player_guess == "B":
            score += 1
            print(f"That's right. Your score is {score}.")
            switch()
        elif choice_A > choice_B and player_guess == "B":
            print(f"Game over. Final score: {score}")
            game_continue = False
        elif choice_A < choice_B and player_guess == "A":
            print(f"Game over. Final score: {score}")
            game_continue = False
        else:
            print("Error 1.")
            game_continue = False
game()

# if right, move B person to A position


# if right, loop back to move B to A


