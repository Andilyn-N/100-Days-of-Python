logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)

game_continue = True
secret_bids = {}
while game_continue:
    namez = input("What is your name?")
    bid_num = input("What is your bid?")

    secret_bids[namez] = bid_num

    restart_question = input("Are there any more bidders?").lower()
    print("\n" * 100)
    if restart_question == "no":
        game_continue = False
        winner_name = max(secret_bids)
        winning_bid = secret_bids[winner_name]
        print(f"The winner is {winner_name} with a bet of ${winning_bid}!")