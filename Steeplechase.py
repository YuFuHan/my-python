"""
File: Steeplechase.py
Name: TODO:
---------------------------------
TODO:
"""

from karel.stanfordkarel import *
def turn_right():
    for i in range(3):
        turn_left()
def jump():
    up()
    cross()
    down()
def up():
    while not facing_north():
        turn_left()
    while not right_is_clear():
        move()
def cross():
    turn_right()
    move()
    turn_right()
def down():
    while front_is_clear():
        move()
def main():
    """
    Karel crosses hurdles in a 12x12 world
    with a for loop 
    """
    for i in range(11):
        if front_is_clear():
            move()
        else:
            jump()













####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
