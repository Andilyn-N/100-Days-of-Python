while not at_goal():
    if right_is_clear():
        turn_left()
        turn_left()
        turn_left()
        move()
    elif front_is_clear():
        move()
    elif wall_in_front():
        turn_left()

# Robot will get stuck in infinite loop depending on starting point
# Will need to debug after day 15