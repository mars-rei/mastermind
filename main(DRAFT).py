import sys, random

from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, TypeAlias, Optional, NoReturn
# ^^^^^^^^^^ IMPORTS ^^^^^^^^^^


# Information
"""
---------- CMP5361 - Computer Mathematics and Declarative Programming ----------

Project: Mastermind Command Line Game

Authors:
- Imogen Dicen (23127176)
- Angelo Luis Lagdameo (23134228)

"""


# ----- Interface Visuals -----
mastermind_intro : str = """
 ___________________________________
|     MASTERMIND - Command Line     |
|___________________________________|
"""

main_menu_options : str = """
MAIN MENU ---------------------------

(0) Single Player
(1) Multiplayer
(2) Campaign
(3) Exit
"""


# ----- Program Flow and Functions -----


# TODO: parseMenuOption to deal with match-case instead of recieveMenuInput?
def recieve_menu_input() -> None:
    #DRAFT (as well)
    """
    i = int(input(">"))
    if i == 0:
        print("SinglePlayer Mode")
    elif i == 1:
        print("Multiplayer Mode")
    elif i == 2:
        print("Campaign Mode")
    else:
        print("Invalid Choice!")
    """
        
    #DRAFT for logic
    try:
        i = int(input(">"))

        match i:
            case 0:
                # TODO - Document/Create start_single_player Function
                print("SinglePlayer Mode")
            case 1:
                # TODO - Document/Create start_multiplayer Function
                print("Multiplayer Mode")
            case 2:
                # TODO - Document/Create start_campaign Function
                print("Campaign Mode")
            case 3:
                print("Exiting Mastermind...")
                exit()
    except ValueError:
        print("ERROR: Invalid Input")


# Prints Game Title & Main Menu
def display_mastermind_intro() -> None:
    print(mastermind_intro + main_menu_options)

# Combines Interface display and Running Prompt
def main_menu_navigation() -> None:
    display_mastermind_intro()

    while True:
        recieve_menu_input()


if __name__=="__main__":
    main_menu_navigation()