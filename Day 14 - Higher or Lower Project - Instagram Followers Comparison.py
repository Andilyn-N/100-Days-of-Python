logo = r"""
    __  ___       __             
   / / / (_)___ _/ /_  ___  _____
  / /_/ / / __ `/ __ \/ _ \/ ___/
 / __  / / /_/ / / / /  __/ /    
/_/ ///_/\__, /_/ /_/\___/_/     
   / /  /____/_      _____  _____
  / /   / __ \ | /| / / _ \/ ___/
 / /___/ /_/ / |/ |/ /  __/ /    
/_____/\____/|__/|__/\___/_/     
"""

vs = r"""
 _    __    
| |  / /____
| | / / ___/
| |/ (__  ) 
|___/____(_)
"""

from game_data import data
import random

print(logo)

def chooser(account_1, account_2):
    name_1 = account_1["name"]
    description_1 = account_1["description"]
    followers_1 = account_1["follower_count"]
    country_1 = account_1["country"]
    name_2 = account_2["name"]
    description_2 = account_2["description"]
    followers_2 = account_2["follower_count"]
    country_2 = account_2["country"]

    print(f"Compare A: {name_1}, a {description_1} from {country_1}.")
    print(vs)
    print(f"Against B: {name_2}, a {description_2} from {country_2}.\n")
    return followers_1, followers_2


def assign(choice_1, choice_2):
    og_choice_2 = choice_2
    while choice_1 == choice_2 or og_choice_2 == choice_2:
        choice_2 = random.choice(data)
    return [choice_1, choice_2]



def game():
    score = 0
    game_continue = True
    random_choice_1 = random.choice(data)
    random_choice_2 = None
    while game_continue is True:
        random_choice_1, random_choice_2 = assign(random_choice_1, random_choice_2)
        followers_1, followers_2 = chooser(random_choice_1, random_choice_2)
        print(f"Your score is {score}.\n")
        player_guess = input("Who has more Instagram followers? Type \"A\" or \"B\":  ").upper()

        if followers_1 > followers_2 and player_guess == "A":
            score += 1
            print(f"\n\n\nThat's right.")
            random_choice_1 = random_choice_2

        elif followers_1 < followers_2  and player_guess == "B":
            score += 1
            print(f"\n\n\nThat's right.")
            random_choice_1 = random_choice_2

        elif followers_1 > followers_2  and player_guess == "B":
            print(f"Wrong. Game over. Score: {score}")
            game_continue = False

        elif followers_1 < followers_2 and player_guess == "A":
            print(f"Wrong. Game over. Score = {score}")
            game_continue = False

        else:
            print(f"Invalid entry. Game over. Score = {score}")
            game_continue = False
game()




