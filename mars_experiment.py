# separate file for mars testing (all in one file)


# ------ Imports ------
from __future__ import annotations
import sys, random
from dataclasses import dataclass
from enum import Enum
from typing import Type, Any, Callable, TypeAlias, Optional, NoReturn


# ------ Information -------
"""
---------- CMP5361 - Computer Mathematics and Declarative Programming ----------

Project: Mastermind Command Line Game

Authors:
- Imogen Dicen (23127176)
- Angelo Luis Lagdameo (23134228)

"""


# ----- Main Menu Option Type -----

class Main_Menu_Option(Enum):
    Single_Player = 0
    Multiplayer = 1
    Campaign = 2
    Exit = 3
 
    # we'll need to be more specific (as in defining the type through if statements?)
    @classmethod    
    def parse_main_menu_option(cls : Type[Main_Menu_Option], prmpt : str) -> Main_Menu_Option:
        try:
            print(prmpt)
            main_menu_option: Main_Menu_Option = Main_Menu_Option(int(input("> ")))
            return main_menu_option
        except ValueError:
            print("That is an invalid main menu choice.")    


# ----- Code Peg Option Type -----

class Code_Peg_Option(Enum):
    Empty = 0
    Orange = 1
    Green = 2
    Blue = 3
    Yellow = 4
    Purple = 5
    Brown = 6
 
    @classmethod    
    def parse_code_peg_option(cls : Type[Code_Peg_Option], prmpt : str) -> Code_Peg_Option:
        try:
            print(prmpt)
            code_peg_option: Code_Peg_Option = Code_Peg_Option(int(input("> ")))
            if code_peg_option == Code_Peg_Option.Empty:
                print("That is an invalid code peg choice.") 
            else:
                return code_peg_option
        except ValueError:
            print("That is an invalid code peg choice.") 

    def __str__(self):
        return self.name.lower()              


# ----- Interface Visuals -----

mastermind_intro : str = """
 ___________________________________
|     MASTERMIND - Command Line     |
|___________________________________|
"""


# ----- Program Flow and Functions -----


main_menu_options : str = """
MAIN MENU ---------------------------

(0) Single Player
(1) Multiplayer
(2) Campaign
(3) Exit

Enter an option (0-3): 
"""

code_peg_options : str = """
CODE PEG SELECTION ---------------------------

(1) Orange
(2) Green
(3) Blue
(4) Yellow
(5) Purple
(6) Brown

Enter an option (1-6): 
"""

def recieve_main_menu_input() -> None:
    selected_option = Main_Menu_Option.parse_main_menu_option(main_menu_options)
    print()

    match selected_option:
        case Main_Menu_Option.Single_Player:
            # TODO - Document/Create start_single_player Function
            print("Starting single player mode...")
        case Main_Menu_Option.Multiplayer:
            # TODO - Document/Create start_multiplayer Function
            print("Starting multiplayer mode...")
        case Main_Menu_Option.Campaign:
            # TODO - Document/Create start_campaign Function
            print("Starting campaign mode...")
        case Main_Menu_Option.Exit:
            print("Exiting Mastermind...")
            exit()
        case _:
            print("Invalid input.")

def recieve_code_peg_input() -> None:
    selected_option = Code_Peg_Option.parse_code_peg_option(code_peg_options)
    if selected_option != None:
        print("You have chosen an " + str(selected_option) + " peg.") if selected_option == Code_Peg_Option.Orange else print("You have chosen a " + str(selected_option) + " peg.")

# Prints Game Title & Main Menu
def display_mastermind_intro() -> None:
    print(mastermind_intro)

# Combines Interface display and Running Prompt
def main_menu_navigation() -> None:
    display_mastermind_intro()

    while True:
        recieve_code_peg_input()


if __name__=="__main__":
    main_menu_navigation()