logo = r"""
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
print(logo)
import random

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_hand = []
computer_hand = []

game_continue = True
game_not_over = True
game_end = False

random.shuffle(cards)
player_hand.append(cards[0])
player_hand.append(cards[1])
random.shuffle(cards)
computer_hand.append(cards[0])

print(player_hand)
print(computer_hand)
while game_continue:
    total_player_hand = sum(player_hand)
    total_computer_hand = sum(computer_hand)
    if player_hand[0] + player_hand[1] == 21:
        print("Blackjack! You are the winner!")
        game_continue = False
        # working
    else:
        choice_1 = input("Would you like to hit or stand?\n").lower()
        random.shuffle(cards)
        total_computer_hand += cards[0]
        if choice_1 == "stand":
            print(f"This is the computer1 {total_computer_hand}")
            print(f"This is the player {total_player_hand}")
        elif choice_1 == "hit"
            print(f"This is the computer1 {total_computer_hand}")
            print(f"This is the player {total_player_hand}")
    if total_computer_hand == 21:
        game_continue = False
        print("Computer wins1!")
        #working
    elif total_computer_hand > total_player_hand and total_computer_hand < 21:
        game_continue = False
        print("Computer wins2!")
        #working
    elif total_computer_hand < 21:
        while total_computer_hand < 17:
            random.shuffle(cards)
            total_computer_hand += cards[0]
            print(f"This is the computer running total3 {total_computer_hand}")
            # working
        if total_computer_hand == 21:
            game_continue = False
            print("Computer wins1.5!")
            # working
        elif total_computer_hand > total_player_hand and total_computer_hand < 21:
            game_continue = False
            print("Computer wins2.5!")
            # working
        elif total_computer_hand > 21:
            print("Computer busted. You win6!")
            # working
            game_continue = False
        elif total_computer_hand >= 17 and total_computer_hand < 21 and total_computer_hand > total_player_hand:
            print(f"Computer wins!4")
            game_continue = False
            #
        elif total_computer_hand >= 17 and total_computer_hand < 21 and total_computer_hand < total_player_hand:
            print("You win5")
            game_continue = False
            #working
        # elif total_computer_hand == total_player_hand and total_computer_hand < 17:
        #     random.shuffle(cards)
        #     total_computer_hand += cards[0]
        #     print(f"This is the computer7 {total_computer_hand}")
        #     #
        elif total_computer_hand == total_player_hand and total_computer_hand >= 17:
            print("Standoff!9")
            game_continue = False
            #working
    else:
        print("Computer busts!10")
        game_continue = False
        #working
       
# while game_continue:



# if restart_question == "n":
#     game_continue = False
#     print("Goodbye.")

# if game_continue:
#     play_again = input("Would you like to play again? y/n\n").lower()
#     if play_again == "n":
#         game_continue = False
#         game_end = False
#         print("Goodbye.")


# bust_check will take the max of both hands
# def bust_check():
#     return max(player_hand, computer_hand)

# def ace_reduction():
#     if player_hand[0] == 11:
#         return player_hand[0] - 10
# print(bust_check())

# print(ace_reduction())

