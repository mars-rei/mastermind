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

# -------------------------- use match cases here instead? ---------------------------------------              
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

# -------------------------- use match cases here instead? ---------------------------------------                    
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

# -------------------------- use match cases here instead? ---------------------------------------                         
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

def receive_main_menu_input() -> None:

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
  

def normal_secret_code() -> Secret: # okay
    valid_code_pegs: list[Code] = [peg for peg in Code if peg != Code(0)]
    newSecretCode: Secret = tuple(random.sample(valid_code_pegs, k=4))
    return newSecretCode

def make_secret_code() -> Secret:
    pass

def hard_secret_code() -> Secret: # okay
    valid_code_pegs: list[Code] = [peg for peg in Code if peg != Code(0)]
    no_duplicate_sample: list[Code] = random.sample(valid_code_pegs, k=3)
    duplicate_code: list[Code] = no_duplicate_sample + [no_duplicate_sample[2]]
    newSecretCode: Secret = tuple(random.sample(duplicate_code, k=4))
    return newSecretCode 


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
        #game_session: tuple[bool, Player] = play_round(game_board, players, secret_code)
    else:
        print(f"\nATTEMPT NO.#{turn_count} ----------")
        round: tuple[Board, bool] = play_round(game_board, players, secret_code)
        return play_game(round[0], players, secret_code, turn_count+1, round[1])


# TODO: angelo :3
def start_gameplay(game_mode: Main_Menu_Option, game_board: Board, players: tuple[Player, Player], secret_code: Union[Secret, tuple[Secret, Secret, Secret]]) -> None:
    if game_mode == "Single_Player" or "Multiplayer":
        game_session: tuple[bool, tuple] = play_game(game_board, players, secret_code)
        #play_game(game_mode, game_board, players, secret_code)
        announce_winner(game_session[0], players)









def start_campaign() -> None: # dunno if still needed
    pass


def get_guess(guess_size: int = 1) -> Guess:
    print() # just for formatting - need to figure out
    print(f"Choice for Code Peg No.#{guess_size}")
    if guess_size == 4:
        return (receive_code_peg_input(),)
    else:
        return (receive_code_peg_input(),) + get_guess(guess_size+1)


# marsy is working on get_feedback -------------------------------------------------------------------------------------------------------------------------

# functional and declarative version
"""
def get_feedback(guess: Guess, secret: Secret, code_difficulty: str) -> tuple[bool, Feedback]:
    if guess == secret:
        return [True, tuple([Hint.Red] * 4)]
    else:
        red : Feedback = tuple(get_red_hints(guess, secret))
        print('red hint pegs:', red)
        return [False, None]
    
def get_red_hints(guess: Guess, secret: Secret) -> list:
    return [(Hint.Red, guess[i]) if guess[i] == secret[i] else (Hint.Empty, guess[i]) for i in range(len(guess))]
"""

# imperative version (code_difficulty for brain aid)

def get_feedback(guess : Guess, secret: Secret, code_difficulty: str) -> list[bool, Feedback]:
    if guess == secret:
        feedback : Feedback = (Code_Peg_Option.Red, Code_Peg_Option.Red, Code_Peg_Option.Red, Code_Peg_Option.Red)
        return [True, feedback]
    else:
        red_feedback = []
        for i in range(len(guess)):
            if guess[i] == secret[i]:
                red_feedback.append([str(Hint.Red), str(guess[i])])
            else:
                red_feedback.append([str(Hint.Empty), str(guess[i])])

        white_feedback = [] 
        for i in range(len(guess)):
            if guess[i] in secret:
                if code_difficulty == "normal":
                    if [str(Hint.Red), str(guess[i])] in red_feedback:
                        white_feedback.append([str(Hint.Empty), str(guess[i])])
                    elif [str(Hint.White), str(guess[i])] in white_feedback:
                        white_feedback.append([str(Hint.Empty), str(guess[i])])
                    else:
                        white_feedback.append([str(Hint.White), str(guess[i])])

                if code_difficulty == "hard":
                    secret_occurrences = secret.count(guess[i]) # checks for duplicated peg

                    if secret_occurrences == 2: # if it is the duplicated peg
                        if red_feedback.count([str(Hint.Red), str(guess[i])]) == 2: # if duplicated pegs have both been matched
                            white_feedback.append([str(Hint.Empty), str(guess[i])])
                        elif white_feedback.count([str(Hint.White), str(guess[i])]) == 2: # if duplicated pegs have both been guessed in wrong place
                            white_feedback.append([str(Hint.Empty), str(guess[i])])

                        elif red_feedback.count([str(Hint.Red), str(guess[i])]) == 1 and white_feedback.count([str(Hint.White), str(guess[i])]) == 1:
                            white_feedback.append([str(Hint.Empty), str(guess[i])]) # both pegs have been guessed
                        else:
                            white_feedback.append([str(Hint.White), str(guess[i])]) # only make white if both pegs haven't been guessed
                        
                    elif secret_occurrences == 1: # isn't a duplicated peg (i think i could use an else here instead)
                        # same as for the normal
                        if [str(Hint.Red), str(guess[i])] in red_feedback:
                            white_feedback.append([str(Hint.Empty), str(guess[i])])
                        elif [str(Hint.White), str(guess[i])] in white_feedback:
                            white_feedback.append([str(Hint.Empty), str(guess[i])])
                        else:
                            white_feedback.append([str(Hint.White), str(guess[i])])

            else:
                white_feedback.append([str(Hint.Empty), str(guess[i])])

        feedback = []
        for i in range(len(guess)):
            if red_feedback[i][0] == "red":
                feedback.append(Hint.Red)
            elif white_feedback[i][0] == "white":
                feedback.append(Hint.White)
            else:
                feedback.append(Hint.Empty)

        feedback_order = {Hint.Red: 0, Hint.White: 1, Hint.Empty: 2}
        feedback_sorted = sorted(feedback, key=lambda x: feedback_order[x])

        return [False, tuple(feedback_sorted)]

# ----------------------------------------------------------------------------------------------------------------------------------------------------------
            


def display_board(game_board: Board):
    pass


def update_board(game_board: Board, update: Union[Guess, Feedback]) -> Board:
    pass


def announce_winner(game_finished: bool, players: list) -> None: # okay
    match game_finished:
        case True:
            print(players[0], "has won the game!")
        case False:
            print(players[1], "has won the game!")



# ---------- Program Start Flow ----------
if __name__=="__main__":
    print(mastermind_intro)

    # Mimi's TEST CODE (for get_feedback)
    """
    print()
    print()
    print()

    secret_code : Secret = normal_secret_code()
    guess: Guess = get_guess()
    print('the guess is:', guess[0], guess[1], guess[2], guess[3])

    print('the normal secret code is:', secret_code[0], secret_code[1], secret_code[2], secret_code[3])
    feedback: tuple = get_feedback(guess, secret_code, "normal")
    print('is game finished?:', feedback[0])
    print('feedback:', feedback[1][0], feedback[1][1], feedback[1][2], feedback[1][3])

    print()
    print()
    print()

    secret_code : Secret = hard_secret_code()
    guess: Guess = get_guess()
    print('the guess is:', guess[0], guess[1], guess[2], guess[3])

    print('the hard secret code is:', secret_code[0], secret_code[1], secret_code[2], secret_code[3])
    feedback: tuple = get_feedback(guess, secret_code, "hard")
    print('is game finished?:', feedback[0])
    print('feedback:', feedback[1][0], feedback[1][1], feedback[1][2], feedback[1][3])

    print()
    print()
    print()
    """

    # Gelo's TEST CODE (for start_gameplay)
    while True:
        receive_main_menu_input()


    