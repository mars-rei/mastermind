# ------ Imports ------
from __future__ import annotations
import sys, random
from dataclasses import dataclass
from enum import Enum
from typing import Type, Any, Callable, TypeAlias, Optional, NoReturn, Union


# ------ Information -------
"""
---------- CMP5361 - Computer Mathematics and Declarative Programming ----------

Project: Mastermind Command Line Game

Authors:
- Imogen Dicen (23127176)
- Angelo Luis Lagdameo (23134228)

"""


# ---------- Main Menu Option Type ----------

class Main_Menu_Option(Enum):
    Single_Player = 0
    Multiplayer = 1
    Campaign = 2
    Exit = 3
 
    @classmethod    
    def parse_main_menu_option(cls : Type[Main_Menu_Option], input : str) -> Main_Menu_Option:

        '''
        Main_Menu_Option.parse_main_menu_option is a function
            which parses an input string to a Main_Menu_Option value

        Parameters:
            input (str) : An input string to try to parse into a Main_Menu_Option

        Returns:
            Type[Main_Menu_Option] the function parses the input to a valid
                Main_Menu_Option or prints an error value
        '''
                
        try:
            main_menu_option: Main_Menu_Option = Main_Menu_Option(int(input))
            return main_menu_option
        except ValueError:
            print("That is an invalid main menu choice.")

Menu: TypeAlias = Main_Menu_Option


# ---------- Confirmation Option Type ----------

class Confirmation_Option(Enum):
    Yes = 'y'
    No = 'n'
 
    @classmethod    
    def parse_confirmation_option(cls : Type[Confirmation_Option], input : str) -> Confirmation_Option:

        '''
        Confirmation_Option.parse_confirmation_option is a function
            which parses an input string to a Confirmation_Option value

        Parameters:
            input (str) : An input string to try to parse into aConfirmation_Option

        Returns:
            Type[Confirmation_Option] the function parses the input to a valid
                Cnfirmation_Option or prints an error value
        '''
                
        try:
            confirmation_option: Confirmation_Option = Confirmation_Option(input).lower()
            return confirmation_option
        except ValueError:
            print("That is an invalid confirmation choice.")

Confirm: TypeAlias = Confirmation_Option

# The optional type itself could be used here 


# ---------- Code Peg Option Type ----------

class Code_Peg_Option(Enum):
    Orange = 1
    Green = 2
    Blue = 3
    Yellow = 4
    Purple = 5
    Brown = 6
 
    @classmethod    
    def parse_code_peg_option(cls : Type[Code_Peg_Option], input : str) -> Code_Peg_Option:

        '''
        Code_Peg_Options.parse_code_peg_option is a function
            which parses an input string to a Code_Peg_Option value

        Parameters:
            input (str) : An input string to try to parse into a Code_Peg_Option

        Returns:
            Type[Code_Peg_Option] the function parses the input to a valid
                Code_Peg_Option or prints an error value
        '''
                
        try:
            code_peg_option: Code_Peg_Option = Code_Peg_Option(int(input))
            if code_peg_option == Code_Peg_Option.Empty:
                print("That is an invalid code peg choice.") 
            else:
                return code_peg_option
        except ValueError:
            print("That is an invalid code peg choice.") 

    def __str__(self):
        return self.name.lower()  

Code: TypeAlias = Code_Peg_Option 


# ---------- Hint Peg Type ----------

class Hint_Peg(Enum):
    Empty = 0
    White = 1
    Red = 2
 
    @classmethod    

    def __str__(self):
        return self.name.lower()  

Hint: TypeAlias = Hint_Peg


# ---------- Player Types ----------

@dataclass(eq=True, frozen=True)
class CodeMaker:
    def __str__(self) -> str:
        return "Code Maker"

@dataclass(eq=True, frozen=True)
class CodeBreaker:
    def __str__(self) -> str:
        return "Code Breaker"

@dataclass(eq=True,frozen=True)
class CPU:
    def __str__(self) -> str:
        return "CPU"

Player : TypeAlias = CodeMaker | CodeBreaker | CPU


# ---------- Secret Code Type ----------
Secret: TypeAlias = tuple[Code, Code, Code, Code]
emptySecret : Secret = tuple[Code.Empty, Code.Empty, Code.Empty, Code.Empty]


# ---------- Guess Type ----------
Guess: TypeAlias = tuple[Code, Code, Code, Code]
emptyGuess : Guess = tuple[Code.Empty, Code.Empty, Code.Empty, Code.Empty]


# ---------- Feedback Type ----------
Feedback: TypeAlias = tuple[Hint, Hint, Hint, Hint]
emptyFeedback : Feedback = tuple[Hint.Empty, Hint.Empty, Hint.Empty, Hint.Empty]


# ---------- Row Type ----------
Row: TypeAlias = tuple[Guess, Feedback]
emptyRow: Row = tuple[emptyGuess, emptyFeedback]


# ---------- Board Type ----------
Normal_Board: TypeAlias = tuple[Row, Row, Row, Row, Row, Row]
Hard_Board: TypeAlias = tuple[Row, Row, Row, Row] 
Board: TypeAlias = Normal_Board | Hard_Board

empty_normal_board: Normal_Board = tuple[emptyRow, emptyRow, emptyRow, emptyRow, emptyRow, emptyRow]
empty_hard_board: Hard_Board = tuple[emptyRow, emptyRow, emptyRow, emptyRow]


# ---------- Interface Visuals ----------

mastermind_intro : str = """
 ___________________________________
|     MASTERMIND - Command Line     |
|___________________________________|
"""


# ---------- Option Interface Visuals ----------

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

# ---------- Option Interface Visuals ----------

def recieve_main_menu_input() -> None:

    '''
        recieve_main_menu_input is a function
            which recieves the user's parsed Main_Menu_Option and 
            based on this, calls the appropriate main menu option function
    '''
    
    print(main_menu_options)
    selected_option = Main_Menu_Option.parse_main_menu_option(input("> "))
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


def recieve_code_peg_input() -> Code: 

    '''
        recieve_code_peg_input is a function
            which recieves the user's parsed Code_Peg_Option and 
            based on this, print out the appropriate message to 
            the command-line
    '''

    print(code_peg_options)
    selected_option = Code_Peg_Option.parse_code_peg_option(input("> "))
    print()

    match selected_option:
        case Code_Peg_Option.Orange:
            print("You have chosen an orange peg.")
            selected_option : Code = selected_option
            return selected_option
        case Code_Peg_Option.Green:
            print("You have chosen a green peg.")
            selected_option : Code = selected_option
            return selected_option
        case Code_Peg_Option.Blue:
            print("You have chosen a blue peg.")
            selected_option : Code = selected_option
            return selected_option
        case Code_Peg_Option.Yellow:
            print("You have chosen a yellow peg.")
            selected_option : Code = selected_option
            return selected_option
        case Code_Peg_Option.Purple:
            print("You have chosen a purple peg.")
            selected_option : Code = selected_option
            return selected_option
        case Code_Peg_Option.Brown:
            print("You have chosen a brown peg.")
            selected_option : Code = selected_option
            return selected_option


def recieve_confirmation_input() -> Confirmation_Option: # TO DO

    '''
        recieve_confirmation_input is a function
            which recieves the user's parsed Confirm_Option and 
            based on this, ...?
    '''

    print("Are you sure you want to continue?") # will probably change later on
    selected_option = Confirmation_Option.parse_confirmation_option(input("> "))
    print()

    match selected_option:
        case Confirmation_Option.Yes:
            print("????")
        case Confirmation_Option.No:
            print("????")
  

def normal_secret_code() -> Secret: 
    valid_code_pegs: list = [peg for peg in Code if peg != Code(0)]
    newSecretCode: Secret = random.sample(valid_code_pegs, k=4)
    return newSecretCode

def make_secret_code() -> Secret:
    pass

def hard_secret_code() -> Secret: 
    valid_code_pegs: list = [peg for peg in Code if peg != Code(0)]
    newSecretCode: list = random.sample(valid_code_pegs, k=3)
    newSecretCode.append(newSecretCode[2])
    random.shuffle(newSecretCode)
    newSecretCode : Secret
    return newSecretCode

def start_single_player() -> None:
    game_board: Normal_Board = empty_normal_board
    players = [CodeBreaker, CPU]
    game_finished : bool = False

    secret_code : Secret = normal_secret_code()

    max_turns : int = 6
    turn_count : int = 0

    while turn_count < max_turns:
        display_board(game_board)
        new_guess : Guess = get_guess()

        game_board : Normal_Board = update_board(game_board, turn_count, new_guess)

        state_and_feedback : list = get_feedback(new_guess, secret)
        game_finished : bool = state_and_feedback[0]
        new_feedback : Feedback = state_and_feedback[1]

        game_board : Normal_Board = update_board(game_board, turn_count, new_feedback)

        turn_count += 1

        if game_finished:
            break

    announce_winner(game_finished, players)

def start_multiplayer() -> None:
    pass

def start_campaign() -> None:
    pass

def get_guess() -> Guess:
    guess : list = []
    while len(guess) != 4:
        potentialPeg = recieve_code_peg_input()
        if potentialPeg != None:
            guess.append(potentialPeg)
        
    guess : Guess

    # add confirmation

    return guess

def get_feedback(guess: Guess, secret: Secret) -> list[bool, Feedback]:
    pass

def display_board(game_board: Board):
    pass

def update_board(game_board: Board, turn_count: int, update: Union[Guess, Feedback]) -> Board:
    pass

def announce_winner(game_finished: bool, players: list) -> None:
    if game_finished:
        print(players[0], "has won the game!")
    else:
        print(players[1], "has won the game!")



# ---------- Program Start Flow ----------
if __name__=="__main__":
    print(mastermind_intro)

    #while True:
        #recieve_main_menu_input()
    secret : Secret = normal_secret_code()
    print('normal secret code:', secret[0], secret[1], secret[2], secret[3])

    secret : Secret = hard_secret_code()
    print('hard secret code:', secret[0], secret[1], secret[2], secret[3])

    guess: Guess = get_guess()
    print('guess:', guess[0], guess[1], guess[2], guess[3])
