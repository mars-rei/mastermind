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
    Single_Player = 1
    Multiplayer = 2
    Campaign = 3
    Exit = 4
 
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

class Confirmation_Option(Enum): # maybe just use discriminated unions instead and have different options for yes and no?
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


# ---------- Code Peg Option Type ----------

class Code_Peg_Option(Enum):
    # optional type instead of empty
    Empty = 0
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
    Empty = 0 # use optional type instead?
    White = 1
    Red = 2
 
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

(1) Single Player
(2) Multiplayer
(3) Campaign
(4) Exit

Enter an option (1-4): 
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

def receive_main_menu_input() -> None: # TODO

    '''
        receive_main_menu_input is a function
            which receives the user's parsed Main_Menu_Option and 
            based on this, calls the appropriate main menu option function
    '''
    
    print(main_menu_options)
    selected_option = Main_Menu_Option.parse_main_menu_option(input("> "))
    print()

    match selected_option:
        case Main_Menu_Option.Single_Player:
            # TODO - Document/Create start_single_player Function
            start_gameplay(selected_option, empty_normal_board, (CodeBreaker, CPU), normal_secret_code())
        case Main_Menu_Option.Multiplayer:
            # TODO - Document/Create start_multiplayer Function
            print("Starting multiplayer mode...")
        case Main_Menu_Option.Campaign:
            # TODO - Document/Create start_campaign Function
            print("Starting campaign mode...")
        case Main_Menu_Option.Exit:
            print("Exiting Mastermind...")
            exit()


# marsy's suggestion to new program flow
"""def receive_main_menu_input() -> Main_Menu_Option:
    print(main_menu_options)
    selected_option = Main_Menu_Option.parse_main_menu_option(input("> "))
    print()

    match selected_option:
        case Main_Menu_Option.Single_Player:
            return Main_Menu_Option.Single_Player
        case Main_Menu_Option.Multiplayer:
            return Main_Menu_Option.Multiplayer
        case Main_Menu_Option.Campaign:
            return Main_Menu_Option.Campaign
        case Main_Menu_Option.Exit:
            print("Exiting Mastermind...")
            exit()"""


def receive_code_peg_input() -> Code: 

    '''
        receive_code_peg_input is a function
            which receives the user's parsed Code_Peg_Option and 
            based on this, print out the appropriate message to 
            the command-line
    '''

    while True:
        print(code_peg_options)
        selected_option = Code_Peg_Option.parse_code_peg_option(input("> "))

        if selected_option:
            match selected_option:
                case Code_Peg_Option.Orange:
                    print("You have chosen an orange peg.")
                case Code_Peg_Option.Green:
                    print("You have chosen a green peg.")
                case Code_Peg_Option.Blue:
                    print("You have chosen a blue peg.")
                case Code_Peg_Option.Yellow:
                    print("You have chosen a yellow peg.")
                case Code_Peg_Option.Purple:
                    print("You have chosen a purple peg.")
                case Code_Peg_Option.Brown:
                    print("You have chosen a brown peg.")
            return selected_option
        else:
            print("Invalid peg choice.")



def receive_confirmation_input() -> Confirmation_Option: # TO DO

    '''
        receive_confirmation_input is a function
            which receives the user's parsed Confirm_Option and 
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
    valid_code_pegs: list[Code] = [peg for peg in Code if peg != Code(0)]
    newSecretCode: Secret = tuple(random.sample(valid_code_pegs, k=4))
    return newSecretCode


def make_secret_code() -> Secret: # TODO
    pass


def hard_secret_code() -> Secret: 
    valid_code_pegs: list[Code] = [peg for peg in Code if peg != Code(0)]
    no_duplicate_sample: list[Code] = random.sample(valid_code_pegs, k=3)
    duplicate_code: list[Code] = no_duplicate_sample + [no_duplicate_sample[2]]
    newSecretCode: Secret = tuple(random.sample(duplicate_code, k=4))
    return newSecretCode 


# gelo is working on start_gameplay ------------------------------------------------------------------------------------------------------------------------

# IN-PROGRESS function
def play_round(game_board: Board, secret_code: Union[Secret, tuple[Secret, Secret, Secret]]) -> tuple[Board, bool]:    
    display_board(game_board)
    new_guess: Guess = get_guess()
    first_board_update: Board = update_board(game_board, new_guess)
    new_feedback: Feedback = get_feedback(new_guess, secret_code)
    second_board_update: Board = update_board(first_board_update, new_feedback)
    return (second_board_update, new_feedback[0])


# IN-PROGRESS function
def play_game(game_board: Board, players: tuple[Player, Player], secret_code: Union[Secret, tuple[Secret, Secret, Secret]], turn_count: int = 1, game_finished = False) -> bool:
    if turn_count == 7 or game_finished == True:
        return game_finished
    else:
        print(f"\nATTEMPT NO.#{turn_count} ----------")
        round: tuple[Board, bool] = play_round(game_board, players, secret_code)
        return play_game(round[0], players, secret_code, turn_count+1, round[1])


# TODO: angelo :3
def start_gameplay(game_mode: Main_Menu_Option, game_board: Board, players: tuple[Player, Player], secret_code: Union[Secret, tuple[Secret, Secret, Secret]]) -> None:
    if game_mode == "Single_Player" or game_mode == "Multiplayer":
        game_session: tuple[bool, tuple] = play_game(game_board, players, secret_code)
        announce_winner(game_session[0], players)
    if game_mode == "Campaign":
        pass

# ----------------------------------------------------------------------------------------------------------------------------------------------------------


def get_guess(guess_size: int = 1) -> Guess:
    print() # just for formatting - need to figure out
    print(f"Choice for Code Peg No.#{guess_size}")
    if guess_size == 4:
        return (receive_code_peg_input(),)
    else:
        return (receive_code_peg_input(),) + get_guess(guess_size+1)


def get_feedback(guess: Guess, secret: Secret) -> tuple[bool, Feedback]:
    if guess == secret:
        return [True, tuple([Hint.Red] * 4)]
    else:
        red : list = get_red_hints(guess, secret) # structure is a list of tuples
        print('red hint pegs:', red)
        white : list = get_white_hints(guess, secret, red) # structure is a list of tuples
        print('white hint pegs:', white)
        feedback : list[Hint] = join_hints(red, white)
        final_feedback : Feedback = sort_hints(feedback) 
        return [False, final_feedback]


# merges red and white pegs, with empty pegs filling in the spaces
def join_hints(red_pegs : list, white_pegs : Feedback) -> list[Hint]:
    return list(map(lambda i: Hint.Red if red_pegs[i][0] else Hint.White if white_pegs[i][0] else Hint.Empty, range(4)))


def sort_hints(feedback: list[Hint]) -> Feedback: 
    feedback_order = {Hint.Red: 0, Hint.White: 1, Hint.Empty: 2}
    return tuple(sorted(feedback, key=lambda x: feedback_order[x]))

 
def get_red_hints(guess: Guess, secret: Secret) -> list:
    return [(True, guess[i]) if guess[i] == secret[i] else (False, guess[i]) for i in range(len(guess))]


def get_white_hints(guess : Guess, secret : Secret, red_pegs : list) -> Feedback:
    # checks if peg is a duplicated peg in the secret code
    def check_if_dupe(peg : Code, secret : Secret) -> bool: 
        return secret.count(peg) == 2
    

    # checks how many times peg has been matched (red)
    def check_guessed_correctly(peg : Code, red_pegs : list) -> int: 
        return red_pegs.count((True, peg))
    

    # checks how many times peg has almost been matched (white)
    def check_almost_guessed(peg : Code, running_feedback : list) -> int:
        return running_feedback.count((True, peg))
    

    # is a single peg in the secret
    def occurs_once(peg : Code, red_pegs : list, running_feedback : list) -> tuple[bool, Code]:
        return [(check_guessed_correctly(peg, red_pegs) == 0 and check_almost_guessed(peg, running_feedback) == 0), peg]


    # is a duplicate peg in the secret
    def occurs_twice(peg : Code, red_pegs : list, running_feedback : list) -> tuple[bool, Code]:
        return [((check_guessed_correctly(peg, red_pegs) + check_almost_guessed(peg, running_feedback)) < 2), peg]
  

    # recursively runs through guess, assigning white pegs according to secret and red_pegs
    def check_through_guess(guess_left: tuple, running_feedback : list) -> list:
        if not guess_left:
            return running_feedback
        
        current_peg : Code = guess_left[0]

        if current_peg in secret:
            match check_if_dupe(current_peg, secret):
                case True:
                    new_hint : tuple[bool, Code] = occurs_twice(current_peg, red_pegs, running_feedback)

                case False:
                    new_hint : tuple[bool, Code] = occurs_once(current_peg, red_pegs, running_feedback)
                    
        else:
            new_hint : tuple[bool, Code] = (False, current_peg)
        
        return check_through_guess(guess_left[1:], running_feedback + [new_hint])


    feedback : list = check_through_guess(guess, [])
    return feedback
           

def display_board(game_board: Board): # TODO
    pass


# TODO: gelo's doing this
def update_board(game_board: Board, new_guess: Guess, new_feedback: Feedback) -> Board:
    new_row: Row = (Guess, Feedback)
    return game_board + new_row


def announce_winner(game_finished: bool, players: tuple) -> None: 
    match game_finished:
        case True:
            print(players[0], "has won the game!")
        case False:
            print(players[1], "has won the game!")


# ---------- Program Start Flow ----------
if __name__=="__main__":
    print(mastermind_intro) 
    """
    while True:
        receive_main_menu_input()
    """
    # Gelo's TEST CODE (for update_board)
    sample_secret_code: Secret = normal_secret_code()
    sample_board: Board = empty_normal_board
    sample_guess: Guess = get_guess()
    sample_feedback: Feedback = get_feedback(sample_guess, sample_secret_code)
    updated_board: Board = update_board(sample_board, sample_guess, sample_feedback)
    print(updated_board)