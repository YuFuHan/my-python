"""
File: DoubleBeepers.py
Name:游富涵
-------------------------------
"""

from karel.stanfordkarel import *
def turn_back():
    turn_left()
    turn_left()
def double_beeper():
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        put_beeper()
        turn_back()
        move()
        turn_back()
    move()

def main():
    """
    Karel will double the beepers
    """
    move()
    double_beeper()
    turn_back()
    while on_beeper():
        pick_beeper()
        move()
        put_beeper()
        turn_back()
        move()
        turn_back()
    turn_back()















####### DO NOT EDIT CODE BELOW THIS LINE ########

if __name__ == '__main__':
    execute_karel_task(main)