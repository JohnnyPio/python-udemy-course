# See exercises: https://reeborg.ca/reeborg.html?lang=en&mode=python

def turn_around():
    turn_left()
    turn_left()
    
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
def hurdle():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()
    
# Hurdle 1
#for i in range(6):
#    move()
#    hurdle()
    
# Hurdle 2
#while at_goal() == False:
#    move()
#    hurdle()

# Hurdle 3
#while at_goal() != True:
#    if front_is_clear() == True:
#        move()
#    else:
#        hurdle()

# Hurdle 4
#while at_goal() != True:
#    if wall_in_front() == True:
#        turn_left()
#    elif wall_on_right() == True:
#        move()
#    else:
#        turn_right()
#        move()

# Maze - cleaned up
while at_goal() != True:
    if right_is_clear():
        turn_right()
        move()
    elif front_is_clear():
        move()
    else:
        turn_left()

    
    
