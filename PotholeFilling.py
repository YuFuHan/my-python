"""
File: PotholeFilling.py
Name:游富涵
--------------------------
This program shows karel filling 3
potholes. Students learn the concept of
decomposition through the process.
"""

from karel.stanfordkarel import *
def turn_right():
    for i in range(3):
        turn_left()
def put_99():
    for i in range(99):
        put_beeper()
def go_in():
    """
    pre-condition: Karal is at the upper left, facing east.
    post-condition: Karal is in the pothholl, facing south.
    """
    move()
    turn_right()
    move()
def go_out():
    """
    pre-condition: Karal is in the pothholl, facing south.
    post-condition: Karal is at the upper right, facing east.
    """
    turn_right()
    turn_right()
    move()
    turn_right()
    move()
def main():
    while front_is_clear():
        go_in()
        put_99()
        go_out()













####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)
