import sys, random

from dataclasses import dataclass
from enum import Enum
from typing import Any, Callable, TypeAlias, Optional, NoReturn


"""
---------- CMP5361 - Computer Mathematics and Declarative Programming ----------

Project: Mastermind Command Line Game

Authors:
- Imogen Dicen (23127176)
- Angelo Luis Lagdameo (23134228)

"""

mastermind_intro : str = """
-------------------------------------
------------- MASTERMIND ------------
-------------------------------------
"""

main_menu : str = """
MAIN MENU ---------------------------
(1) Single Player
(2) Multiplayer
(3) CAMPAIGN
"""

def display_mastermind_intro() -> None:
    print(mastermind_intro)
    print(main_menu)

def recieve_main_menu_input() -> None:

    
    """
    i = int(input(">"))
    if i == 1:
        print("Choice 1!")
    elif i == 2:
        print("Choice 2!")
    elif i ==3:
        print("Choice 3!")
    else:
        print("Invalid Choice!")
    """

def navigate_main_menu() -> None:
    display_mastermind_intro()
    recieve_main_menu_input()

if __name__=="__main__":
    navigate_main_menu()