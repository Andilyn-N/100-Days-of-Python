love_list1 = ["t","r","u","e"]
love_list2 = ["l","o","v","e"]


def calculate_love_score(name1, name2):
    love_score1 = []
    love_score2 = []
    for letter in name1:
        if letter in love_list1:
            love_score1 += letter
    for letter in name1:
        if letter in love_list2:
            love_score2 += letter
    for letter in name2:
        if letter in love_list1:
            love_score1 += letter
    for letter in name2:
        if letter in love_list2:
            love_score2 += letter
    tensplace = len(love_score1)
    onesplace = len(love_score2)
    print(f"Your love score is {tensplace}{onesplace}!")

calculate_love_score("Kanye West", "Kim Kardashian")