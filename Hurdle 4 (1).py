def jump():
    turn_left()
    while wall_on_right():
         move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    while front_is_clear():
        move()
    turn_left()
while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
        jump()
################################################################
# WARNING: Do not change this comment.
# Library Code is below.
################################################################
