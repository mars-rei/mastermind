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
            lower_confirmation_input: str = input.lower().strip()
            confirmation_option: Confirmation_Option = Confirmation_Option(input)
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
Players : TypeAlias = tuple[CodeBreaker, CodeMaker] | tuple[CodeBreaker, CPU]


# ---------- Secret Code Type ----------
Secret: TypeAlias = tuple[Code, Code, Code, Code]
emptySecret : Secret = tuple[Code.Empty, Code.Empty, Code.Empty, Code.Empty]


# ---------- Guess Type ----------
Guess: TypeAlias = tuple[Code, Code, Code, Code]
emptyGuess : Guess = (Code.Empty, Code.Empty, Code.Empty, Code.Empty) 


# ---------- Feedback Type ----------
Feedback: TypeAlias = tuple[Hint, Hint, Hint, Hint]
emptyFeedback : Feedback = (Hint.Empty, Hint.Empty, Hint.Empty, Hint.Empty) # TEMPORARY: for the purpose of testing update_board()


# ---------- Row Type ----------
Row: TypeAlias = tuple[Guess, Feedback]
#emptyRow: Row = tuple[emptyGuess, emptyFeedback]
emptyRow: Row = (emptyGuess, emptyFeedback) # TEMPORARY: for the purpose of testing update_board()


# ---------- Board Type ----------
Normal_Board: TypeAlias = tuple[Row, Row, Row, Row, Row, Row]
Hard_Board: TypeAlias = tuple[Row, Row, Row, Row] 
Board: TypeAlias = Normal_Board | Hard_Board

#empty_normal_board: Normal_Board = tuple[emptyRow, emptyRow, emptyRow, emptyRow, emptyRow, emptyRow]
empty_normal_board: Normal_Board = (emptyRow, emptyRow, emptyRow, emptyRow, emptyRow, emptyRow) # TEMPORARY: for the purpose of testing update_board()
empty_hard_board: Hard_Board = tuple[emptyRow, emptyRow, emptyRow, emptyRow]


# ---------- Interface Visuals ----------

mastermind_intro : str = """
                     ___________________________________
<<<<<<<<<<<<<<<<<<<<|     MASTERMIND - Command Line     |>>>>>>>>>>>>>>>>>>>>
<<<<<<<<<<<<<<<<<<<<|___________________________________|>>>>>>>>>>>>>>>>>>>>
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

(1) \033[38;5;208mOrange\033[0m
(2) \033[38;5;82mGreen\033[0m
(3) \033[38;5;12mBlue\033[0m
(4) \033[38;5;184mYellow\033[0m
(5) \033[38;5;134mPurple\033[0m
(6) \033[38;5;94mBrown\033[0m

Enter an option (1-6): 
"""


# ---------- Option Interface Visuals ----------
def check_one_dupe(secret_code: Secret, index_position: int = 0, found_dupe: tuple[Secret] = ()) -> bool:
    if index_position == 4 and found_dupe:
        return False
    else:
        if secret_code.count(secret_code[index_position]) == 2 and not found_dupe:
            return check_one_dupe(secret_code, index_position+1, (secret_code[index_position], ) + found_dupe)
        elif secret_code.count(secret_code[index_position]) == 2 and found_dupe:
            return True

def check_triple(secret_code: Secret, index_position: int = 0) -> bool:
    if index_position == 4:
        return False
    else:
        if secret_code.count(secret_code[index_position]) <= 2:
            return check_triple(secret_code, index_position+1)
        elif secret_code.count(secret_code[index_position]) >= 3:
            return True
        else:
            return False
        


def receive_main_menu_input() -> None: # TODO

    '''
        receive_main_menu_input is a function
            which receives the user's parsed Main_Menu_Option and 
            based on this, calls the appropriate main menu option function
    '''
    
    print(main_menu_options)
    selected_option = Main_Menu_Option.parse_main_menu_option(input("> "))
    print()

    player1: Player = CodeBreaker()

    match selected_option:
        case Main_Menu_Option.Single_Player:
            # TODO - Document/Create start_single_player Function
            player2: Player = CPU()
            start_gameplay(selected_option, empty_normal_board, (player1, player2), normal_secret_code())
        case Main_Menu_Option.Multiplayer:
            # TODO - Document/Create start_multiplayer Function
            player2: Player = CPU()
            while True:
                print("\nCODEMAKER: ENTER SECRET CODE -------------------- ")
                custom_secret_code: Secret = make_secret_code()
                confirmation_choice: bool = receive_confirmation_input(custom_secret_code)
                if confirmation_choice == True:
                    triple_flag: bool = check_triple(custom_secret_code)
                    if triple_flag == True:
                        print(f"\nINVALID MESSAGE INPUT --------------------\nYou can't have Three Choices of the same Code Peg in the Secret Code") #"You can't have more than two of the same Code peg in the Secret code"
                    else:
                        one_dupe_only_flag = check_one_dupe(custom_secret_code)
                        if one_dupe_only_flag == True:
                            print(f"\nINVALID MESSAGE INPUT --------------------\nYou can't have Two instances of Duplicates in the Secret Code")
                        else:
                            break
            start_gameplay(selected_option, empty_normal_board, (player1, player2), custom_secret_code)
        case Main_Menu_Option.Campaign:
            # TODO - Document/Create start_campaign Function
            print("Starting campaign mode...")
        case Main_Menu_Option.Exit:
            print("Exiting Mastermind...")
            sys.exit()


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
                    print("You have chosen an \033[38;5;208morange\033[0m peg.")
                case Code_Peg_Option.Green:
                    print("You have chosen a \033[38;5;82mgreen\033[0m peg.")
                case Code_Peg_Option.Blue:
                    print("You have chosen a \033[38;5;12mblue\033[0m peg.")
                case Code_Peg_Option.Yellow:
                    print("You have chosen a \033[38;5;184myellow\033[0m peg.")
                case Code_Peg_Option.Purple:
                    print("You have chosen a \033[38;5;134mpurple\033[0m peg.")
                case Code_Peg_Option.Brown:
                    print("You have chosen a \033[38;5;94mbrown\033[0m peg.")
            return selected_option
        else:
            print("Invalid peg choice.")


def receive_confirmation_input(tupleInput: Union[Guess, Secret]) -> Confirmation_Option: # TO DO

    '''
        receive_confirmation_input is a function
            which receives the user's parsed Confirm_Option and 
            based on this, ...?
    '''

    while True:
        print("\nYour Guess: ")
        print(*(str(peg) for peg in tupleInput))
        print("Are you sure you want to continue?") # will probably change later on
        selected_option = Confirmation_Option.parse_confirmation_option(input("> "))
        print()

        match selected_option:
            case Confirmation_Option.Yes:
                print("\nGuess Confirmed.")
                return True
            case Confirmation_Option.No:
                print("\nGuess Cancelled.")
                return False
  

def normal_secret_code() -> Secret: 
    valid_code_pegs: list[Code] = [peg for peg in Code if peg != Code(0)]
    newSecretCode: Secret = tuple(random.sample(valid_code_pegs, k=4))
    return newSecretCode


def make_secret_code(secret_size=1) -> Secret: # TODO
    print()
    print(f"---------- CODE PEG CHOICE NO.#{secret_size} ----------")
    if secret_size == 4:
        return (receive_code_peg_input(),)
    else:
        return (receive_code_peg_input(),) + get_guess(secret_size+1)


def hard_secret_code() -> Secret: 
    valid_code_pegs: list[Code] = [peg for peg in Code if peg != Code(0)]
    no_duplicate_sample: list[Code] = random.sample(valid_code_pegs, k=3)
    duplicate_code: list[Code] = no_duplicate_sample + [no_duplicate_sample[2]]
    newSecretCode: Secret = tuple(random.sample(duplicate_code, k=4))
    return newSecretCode 


# gelo is working on start_gameplay ------------------------------------------------------------------------------------------------------------------------

# IN-PROGRESS function
def play_round(game_board: Board, secret_code: Union[Secret, tuple[Secret, Secret, Secret]], turn_count: int) -> tuple[Board, bool]:    
    while True:
        display_board(game_board)
        new_guess: Guess = get_guess()
        new_feedback: Feedback = get_feedback(new_guess, secret_code)
        confirmation_choice: Confirmation_Option = receive_confirmation_input(new_guess)
        if confirmation_choice == True:
            updated_board: Board = update_board(game_board, new_guess, new_feedback[1], turn_count)
            display_board(updated_board)
            return (updated_board, new_feedback[0])


# IN-PROGRESS function
def play_game(game_board: Board, players: tuple[Player, Player], secret_code: Union[Secret, tuple[Secret, Secret, Secret]], turn_count: int = 1, game_finished = False) -> bool:
    if turn_count == 7 or game_finished == True:
        return game_finished
    else:
        print(f"\n---------- GUESS ATTEMPT NO.#{turn_count} ----------")
        round: tuple[Board, bool] = play_round(game_board, secret_code, turn_count)
        return play_game(round[0], players, secret_code, turn_count+1, round[1])


# TODO: angelo :3 - IN-PROGRESS function
def start_gameplay(game_mode: Main_Menu_Option, game_board: Board, players: tuple[Player, Player], secret_code: Union[Secret, tuple[Secret, Secret, Secret]]) -> Union[None, bool]:
    print(f"""
                                            _______________
    ----------------------------------------| {game_mode.name.upper()} |----------------------------------------
    ----------------------------------------|   GAME MODE   |----------------------------------------
    ----------------------------------------|_______________|----------------------------------------
            """)
    if game_mode == Main_Menu_Option.Single_Player or game_mode == Main_Menu_Option.Multiplayer:    
        game_session: bool = play_game(game_board, players, secret_code)
        end_game(game_session, players, secret_code)
    if game_mode == Main_Menu_Option.Campaign:
        pass

# ----------------------------------------------------------------------------------------------------------------------------------------------------------


def get_guess(guess_size: int = 1) -> Guess:
    print(f"\n---------- CODE PEG CHOICE NO.#{guess_size} ----------")
    if guess_size == 4:
        return (receive_code_peg_input(),)
    else:
        return (receive_code_peg_input(),) + get_guess(guess_size+1)


def get_feedback(guess: Guess, secret: Secret) -> tuple[bool, Feedback]:
    if guess == secret:
        return [True, tuple([Hint.Red] * 4)]
    else:
        red : list = get_red_hints(guess, secret) # structure is a list of tuples
        white : list = get_white_hints(guess, secret, red) # structure is a list of tuples
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


def get_white_hints(guess : Guess, secret : Secret, red_pegs : list) -> list:
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
           

def display_board(game_board: Board) -> None:

    def format_row(row: Row) -> list[str]:
        header : list[str] = ["|        |        |        |        | |        |        |        |        |"]

        guess: Guess = row[0]
        feedback: Feedback = row[1]

        row_pegs: list[str] = [format_peg(peg) for peg in guess] + ["| "] + [format_peg(peg) for peg in feedback] + ["|"]

        footer : list[str] = ["|        |        |        |        | |        |        |        |        |",
                        " -------- -------- -------- --------   -------- -------- -------- -------- "]

        return "\n".join(header) + "\n" + "".join(row_pegs) + "\n" + "\n".join(footer)


    def format_peg(peg: Union[Code, Hint]) -> str:
        match len(str(peg)):
            case 6:
                return f"| {str(peg)} "
            case _:
                padding: str = " " * (6-len(str(peg)))
                return f"| {str(peg)}{padding} "
            

    header : list[str] = [
        "DISPLAYING BOARD ---------------------------",
        "",
        " GUESS                                 FEEDBACK",
        " -------- -------- -------- --------   -------- -------- -------- -------- "
        ]

    board : list[str] = [format_row(row) for row in game_board]

    print("\n".join(header + board))


def update_board(game_board: Board, new_guess: Guess, new_feedback: Feedback, turn_count: int) -> Board:
    new_row: Row = (new_guess, new_feedback)
    match turn_count:
        case 1:
            return (new_row, ) + game_board[:-1]
        case 2:
            return game_board[:-5] + (new_row, ) + game_board[2:]
        case 3:
            return game_board[:-4] + (new_row, ) + game_board[3:]
        case 4:
            return game_board[:-3] + (new_row, ) + game_board[4:]
        case 5:
            return game_board[:-2] + (new_row, ) + game_board[5:]
        case 6:
            return game_board[0:5] + (new_row, )


def end_game(game_finished: bool, players: tuple, secret: Secret) -> None:
    print("\n---------- SECRET CODE ----------")
    print(*(str(peg) for peg in secret))

    print("\n---------- FINAL RESULTS ----------")
    match game_finished:
        case True:
            print(f"\n{str(players[0])} has won the game!")
        case False:
            print(f"\n{str(players[1])} has won the game!")


# ---------- Program Start Flow ----------
if __name__=="__main__":
    print(mastermind_intro) 

    while True:
        receive_main_menu_input()

    