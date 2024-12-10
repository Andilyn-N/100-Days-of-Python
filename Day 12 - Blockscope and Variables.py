game_level = 3
enemies = ["Skeleton", "Zombie", "Alien"]

# valid code because the "if" statement
# does not create a local scope for the variable "new_enemy"
if game_level < 5:
    new_enemy = enemies[0]

print(new_enemy)

def create_enemy():
    if game_level < 5:
        new_enemy2 = enemies[0]
# without the below print statement being indented,
# it is invalid as it's living outside of the local scope of the "if" statement
print(new_enemy2)

# if you create a variable within a function,
# then the variable will only be available within the function

# if you create a variable within an "if" statement, for loop, while loops, etc
# it does not count as a local scope

# on line 16: code will not print even if properly indented if the game level >= 5
# the code in line 12 would not run, so the variable in line 13
# would not be created nor assigned a value
# this is what causes the error in line 9 and 16
# this is how to satisfy the "undefined variable" (even though it's defined within)

def create_enemy_2():
    new_enemy3 = ""
    if game_level < 5:
        new_enemy3 = enemies[0]

    print(new_enemy3)