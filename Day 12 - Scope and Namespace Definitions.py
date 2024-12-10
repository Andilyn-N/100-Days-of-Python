enemies = 1

def increase_enemies():
    enemies = 2
    print(f"enemies inside function: {enemies}")


increase_enemies()
print(f"enemies outside function: {enemies}")

# local scope
def drink_potion():
    # variable inside the function is only used inside the function
    potion_strength = 2
    print(potion_strength)

drink_potion()
# printing potion_strength would error out because
# it's only inside the function drink_potion
# print(potion_strength) = name error (not defined)

# global scope
player_health = 10

def drinks_potion():
    potion_strength = 2
    # will print player_health because
    # the variable is defined outside of the function
    print(player_health)

drinks_potion()
print(player_health)

# namespace: anything I give a name to
# only valid in certain scopes
# functions can only be called on the same tab line vertically (inside the function)