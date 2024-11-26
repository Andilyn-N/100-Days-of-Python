print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."/ ` . "-._ /______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
direction_1 = input(print("You're at a crossroads. Where do you want to go? \n Type \"left\" or \"right\"\n "))

if direction_1 == "left" or direction_1 == "Left":
    print("You come upon an island.")
    direction_2 = input(print(
        "You can try to swim to the island or wait for a boat. \n Type \"swim\" to attempt to swim or \"wait\" to wait for a boat\n "))

    if direction_2 == "Wait" or direction_2 == "wait":
        print("You waited and a rowboat took you to the island.")
        direction_3 = input(print("A castle appears out of nowhere. There are three doors; one red, one yellow, and one blue.\n Which one do you chose? \n Type \"red\" or \"yellow\" or \"blue\"."))

        if direction_3 == "yellow" or direction_3 == "Yellow":
            print("You've found the treasure room! \n Congratulations!")
        elif direction_3 == "red" or direction_3 == "Red":
            print("You open the door and step inside.\n The door slams behind you and you spontaneously combust. \n Game over.")
        elif direction_3 == "blue" or direction_3 == "Blue":
            print("You open the door and step into a gelatinous cube.\n You are stuck here forever. \n Game over.")
        else:
            print("You did not choose a door and passed out. \n Game over.")

    else:
        print("You got a cramp in your leg and drowned. Game over.")
else:
    print("You got lost in the woods. Game over.")

