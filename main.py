# ------ Imports ------
from __future__ import annotations
import sys, random
from dataclasses import dataclass
from enum import Enum
from typing import Type, TypeAlias, Union


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

        """
        turns string input into Main_Menu_Option

        Parameters:
            cls (Type[Main_Menu_Option]) - The Main_Menu_Option to parse
            input (str) - An input string to parse into a Main_Menu_Option

        Returns:
            Main_Menu_Option - The parsed input
        """

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

        """
        turns string input into Confirmation_Option 

        Parameters:
            cls (Type[Confirmation_Option]) - The Confirmation_Option to parse
            input (str) - An input string to parse into a Confirmation_Option

        Returns:
            Confirmation_Option - The parsed input
        """

        try:
            lower_confirmation_input: str = input.lower().strip() # can't you just put this within Confirmation_Option below? - nested and chained pipelining
            confirmation_option: Confirmation_Option = Confirmation_Option(lower_confirmation_input)
            return confirmation_option
        except ValueError:
            print("That is an invalid confirmation choice.")
    
Confirm: TypeAlias = Confirmation_Option


# ---------- Code Peg Option Type ----------
class Code_Peg_Option(Enum):
    Empty = 0
    Orange = 1
    Green = 2
    Blue = 3
    Yellow = 4
    Purple = 5
    Brown = 6
 
    @classmethod    
    def parse_code_peg_option(cls : Type[Code_Peg_Option], input : str) -> Code_Peg_Option:

        """
        turns string input into Code_Peg_Option

        Parameters:
            cls (Type[Code_Peg_Option]) - The Code_Peg_Option to parse
            input (str) - An input string to parse into a Code_Peg_Option

        Returns:
            Code_Peg_Option - The parsed input
        """

        try:
            code_peg_option: Code_Peg_Option = Code_Peg_Option(int(input))
            if code_peg_option != Code_Peg_Option.Empty:
                return code_peg_option
        except ValueError:
            print("That is an invalid code peg choice.") 

    def __str__(self) -> str:
        """
        gets lowercase of Code_Peg_Option

        Returns:
            str - The lowercase string
        """
        return self.name.lower()  

Code: TypeAlias = Code_Peg_Option 


# ---------- Hint Peg Type ----------
class Hint_Peg(Enum):
    Empty = 0
    White = 1
    Red = 2

    def __str__(self) -> str:
        """
        gets lowercase of Hint_Peg

        Returns:
            str - The lowercase string
        """
        return self.name.lower()

Hint: TypeAlias = Hint_Peg


# ---------- Player Types ----------
@dataclass(eq=True, frozen=True)
class CodeMaker:
    def __str__(self) -> str:
        """
        gets string of CodeMaker

        Returns:
            str - The string representation of the CodeMaker
        """
        return "Code Maker"

@dataclass(eq=True, frozen=True)
class CodeBreaker:
    def __str__(self) -> str:
        """
        gets string of CodeBreaker

        Returns:
            str - The string representation of the CodeBreaker
        """
        return "Code Breaker"

@dataclass(eq=True,frozen=True)
class CPU:
    def __str__(self) -> str:
        """
        gets string of CPU

        Returns:
            str - The string representation of the CPU
        """
        return "CPU"

Player : TypeAlias = CodeMaker | CodeBreaker | CPU
Players : TypeAlias = tuple[CodeBreaker, CodeMaker] | tuple[CodeBreaker, CPU]


# ---------- Secret Code Type ----------
Secret: TypeAlias = tuple[Code, Code, Code, Code]
emptySecret : Secret = (Code.Empty, Code.Empty, Code.Empty, Code.Empty)


# ---------- Guess Type ----------
Guess: TypeAlias = tuple[Code, Code, Code, Code]
emptyGuess : Guess = (Code.Empty, Code.Empty, Code.Empty, Code.Empty) 


# ---------- Feedback Type ----------
Feedback: TypeAlias = tuple[Hint, Hint, Hint, Hint]
emptyFeedback : Feedback = (Hint.Empty, Hint.Empty, Hint.Empty, Hint.Empty)


# ---------- Row Type ----------
Row: TypeAlias = tuple[Guess, Feedback]
emptyRow: Row = (emptyGuess, emptyFeedback) 


# ---------- Board Type ----------
Normal_Board: TypeAlias = tuple[Row, Row, Row, Row, Row, Row]
Hard_Board: TypeAlias = tuple[Row, Row, Row, Row] 
Board: TypeAlias = Normal_Board | Hard_Board

empty_normal_board: Normal_Board = (emptyRow, emptyRow, emptyRow, emptyRow, emptyRow, emptyRow) 
empty_hard_board: Hard_Board = (emptyRow, emptyRow, emptyRow, emptyRow) 


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

confirmation_options : str = """
CONFRIMATION SELECTION ---------------------------

(y) Yes
(n) No

Enter a choice (y or n)
"""


# ---------- Option Interface Visuals ----------
def check_one_dupe_pair_secret(secret_code: Secret, index_position: int = 0, found_dupe: tuple[Secret] = ()) -> bool:
    """
    checks if more than one pair of duplicates are within the secret code combination

    Parameters:
        secret_code (Secret) - the secret code to be checked through
        index_position (int) - used to access the value within the current index of the secret_code
        found_dupe (tuple[Secret]) - stores the value of the first duplicate pair found

    Returns:
        bool - signifies if more than one duplicate pair has been found within the secret_code
    """
    
    if index_position == 4 and found_dupe:
        return False
    else:
        if secret_code.count(secret_code[index_position]) == 2 and not found_dupe:
            return check_one_dupe_pair_secret(secret_code, index_position+1, (secret_code[index_position], ) + found_dupe)
        elif secret_code.count(secret_code[index_position]) == 2 and secret_code[index_position] in found_dupe:
            return check_one_dupe_pair_secret(secret_code, index_position+1, found_dupe)
        elif secret_code.count(secret_code[index_position]) == 2 and found_dupe:
            return True

def check_two_dupe_secret(secret_code: Secret, index_position: int = 0) -> bool:
    """
    checks if more than two of the same color peg appears in the secret code

    Parameters:
        secret_code (Secret) - the secret code to be checked through
        index_position (int) - used to access the value within the current index of the secret_code

    Returns:
        bool - signifies if more than 2 of the same code peg appears in the secret_code
    """
        
    if index_position == 4:
        return False
    else:
        if secret_code.count(secret_code[index_position]) <= 2:
            return check_two_dupe_secret(secret_code, index_position+1)
        elif secret_code.count(secret_code[index_position]) >= 3:
            return True


def receive_main_menu_input() -> None:

    """
    prompts for the main menu option to execute the next state of behaviour in regards to the option chosen

    """

    print(main_menu_options)
    selected_option = Main_Menu_Option.parse_main_menu_option(input("> "))
    print()

    match selected_option:
        case Main_Menu_Option.Single_Player:
            start_gameplay(selected_option, empty_normal_board, (CodeBreaker(), CPU()), normal_secret_code())
        case Main_Menu_Option.Multiplayer:
            while True:
                print("\nCODEMAKER: ENTER SECRET CODE -------------------- ")
                custom_secret_code: Secret = make_secret_code()
                confirmation_choice: bool = receive_confirmation_input(custom_secret_code)
                if confirmation_choice == True:
                    if check_two_dupe_secret(custom_secret_code) == True:
                        print(f"\nINVALID MESSAGE INPUT --------------------\nYou can't have more than two of the same Code Peg in the Secret Code.")
                    else:
                        if check_one_dupe_pair_secret(custom_secret_code) == True:
                            print(f"\nINVALID MESSAGE INPUT --------------------\nYou can't have more than one pair of Duplicates in the Secret Code.")
                        else:
                            break
            start_gameplay(selected_option, empty_normal_board, (CodeBreaker(), CodeMaker()), custom_secret_code)
        case Main_Menu_Option.Campaign:
            start_gameplay(selected_option, (empty_normal_board, empty_normal_board, empty_hard_board), (CodeBreaker(), CPU()), (normal_secret_code(), hard_secret_code(), hard_secret_code()))
        case Main_Menu_Option.Exit:
            print("Exiting Mastermind...")
            sys.exit()


def receive_code_peg_input() -> Code: 
    """
    receives the Player's parsed Code_Peg_Option and prints out the appropriate message to the command-line

    Returns:
        Code - The Player's selected Code peg
    """

    while True:
        print(code_peg_options)
        selected_option = Code_Peg_Option.parse_code_peg_option(input("> "))

        if selected_option:
            match selected_option:
                case Code_Peg_Option.Orange:
                    print("You have chosen an " + print_in_colour(selected_option) + " peg.")
                case _:
                    print("You have chosen a " + print_in_colour(selected_option) + " peg.")
            return selected_option
        else:
            print("Invalid peg choice.")


def receive_confirmation_input(choice: Union[Guess, Secret]) -> bool: 

    """
    receives the Player's parsed Confirm_Option and prints out the appropriate message to the command-line

    Parameters:
        choice (Union[Guess, Secret]) - The user's choice of Guess / Secret code

    Returns: 
        bool - Whether the Player chose Yes or No
        
    """

    while True:
        print(confirmation_options)
        print("Your Choice: ")
        print(*(print_in_colour(peg) for peg in choice))
        print("Are you sure you want to continue?") 
        selected_option = Confirmation_Option.parse_confirmation_option(input("> "))
        print()

        match selected_option:
            case Confirmation_Option.Yes:
                print("\nChoice Confirmed.")
                return True
            case Confirmation_Option.No:
                print("\nChoice Cancelled.")
                return False
  

def normal_secret_code() -> Secret: 
    """
    generates a normal Secret code to be guessed by the CodeBreaker

    Returns:
        Secret - A Secret code made up of 4 unique Code pegs
        
    """
    valid_code_pegs: list[Code] = [peg for peg in Code if str(peg) != "empty"]
    newSecretCode: Secret = tuple(random.sample(valid_code_pegs, k=4))
    return newSecretCode


def make_secret_code(secret_size: int = 1) -> Secret: 
    """
    prompts for four code peg choices to generates secret code combination

    Parameters:
        secret_size (int) - increments until it reaches to a value of 4 to stop prompting

    Returns:
        Secret - tuple consisting four code peg choices
    
    """
    print()
    print(f"---------- CODE PEG CHOICE NO.#{secret_size} ----------")
    if secret_size == 4:
        return (receive_code_peg_input(),)
    else:
        return (receive_code_peg_input(),) + get_guess(secret_size+1)


def hard_secret_code() -> Secret: 
    """
    generates a hard Secret code to be guessed by the CodeBreaker

    Returns:
        Secret - A Secret code made up of 2 unique Code pegs and a pair of duplicate Code pegs
        
    """
    valid_code_pegs: list[Code] = [peg for peg in Code if peg != Code(0)]
    no_duplicate_sample: list[Code] = random.sample(valid_code_pegs, k=3)
    duplicate_code: list[Code] = no_duplicate_sample + [no_duplicate_sample[2]]
    newSecretCode: Secret = tuple(random.sample(duplicate_code, k=4))
    return newSecretCode 


# game_mode is grey here meaning it's not use,, update to remove it and from any calls of play_round?
def play_round(game_board: Board, secret_code: Secret, turn_count: int) -> tuple[Board, bool]:    
    """
    executes a series of operations to carry out single attempt at guessing the secret code

    Parameters:
        game_mode (Main_Menu_Option) - passed into update_board() to govern on how to update the existing game_board
        game_board (Board) - the existing game board to be updated
        secret_code (Secret) - passed into get_feedback() to be compared to the new_guess
        turn_count (int) - passed into update_board() to govern what index of the board to display on

    Returns:
        tuple[Board, bool] - newly updated_board and the finished status of the game is returned

    """
    while True:
        display_board(game_board)
        new_guess: Guess = get_guess()
        confirmation_choice: Confirmation_Option = receive_confirmation_input(new_guess)
        if confirmation_choice == True:
            new_feedback: Feedback = get_feedback(new_guess, secret_code)
            updated_board: Board = update_board(game_board, new_guess, new_feedback[1], turn_count)
            display_board(updated_board)
            return (updated_board, new_feedback[0])


def play_game(game_mode: Main_Menu_Option, game_board: Board, players: tuple[Player, Player], secret_code: Secret, turn_count: int = 1, current_stage: int = 0, game_finished: bool = False) -> tuple[bool, Board]:
    """
    makes a decision to on the amount of repeats are made when carrying out a single Guess prompting process

    Parameters:
        game_mode (Main_Menu_Option) - used to govern the set of attempts available to the CodeBreaker
        game_board (Board) - passed to play_round() for updating
        players (tuple[Player, Player]) - passed into the play_game() for the recursive call
        secret_code (Secret) - passed into play_round() for comparison and play_game() for the recursive call
        turn_count (int) - keeps count of the attempts made and is passed into the play_game() incremented by 1 for the recursive call
        current_stage (int) - used to assert the current stage being played during campaign mode
        game_finished (bool) - governs the game session status

    Returns:
        tuple[bool, Board] - winner of the game and the final state of the Board is returned
        
    """
    if game_mode == Main_Menu_Option.Single_Player or game_mode == Main_Menu_Option.Multiplayer or (game_mode == Main_Menu_Option.Campaign and current_stage == 0 or current_stage == 1):
        if turn_count == 7 or game_finished == True:
            return (game_finished, game_board)
        else:
            print(f"\n---------- GUESS ATTEMPT NO.#{turn_count} ----------")
            round: tuple[Board, bool] = play_round(game_board, secret_code, turn_count)
            return play_game(game_mode, round[0], players, secret_code, turn_count+1, current_stage, round[1])
    elif game_mode == Main_Menu_Option.Campaign and current_stage == 2:
        if turn_count == 5 or game_finished == True:
            return (game_finished, game_board)
        else:
            print(f"\n---------- GUESS ATTEMPT NO.#{turn_count} ----------")
            round: tuple[Board, bool] = play_round(game_board, secret_code, turn_count)
            return play_game(game_mode, round[0], players, secret_code, turn_count+1, current_stage, round[1])


# to revise docstring - parameters
def start_gameplay(game_mode: Main_Menu_Option, game_board: Union[Board, tuple[Board, Board, Board]], players: tuple[Player, Player], secret_code: Union[Secret, tuple[Secret, Secret, Secret]], campaign_flag: bool = True, current_stage: int = 0) -> None:
    """
    decides on the amount of games are played for a certain game mode 

    Parameters:
        game_mode (Main_Menu_Option) - used to govern the flow of gameplay
        game_board (Board) - passed to play_game() for decision making
        players (tuple[Player, Player]) - consists of the players of the game
        secret_code (Secret or tuple[Secret, Secret, Secret]) - secret code(s) to be passed into play_game() and displayed through end_game()
        campaign_flag (bool) - signifies when to stop the recursion for campaign mode
        current_stage (int) - used to change game board and the secret code being passed for the next stage of campaign mode

    """
    print(f"""
                                             _______________
    ----------------------------------------| {game_mode.name.upper()} |----------------------------------------
    ----------------------------------------|   GAME MODE   |----------------------------------------
    ----------------------------------------|_______________|----------------------------------------
            """)
    if game_mode == Main_Menu_Option.Single_Player or game_mode == Main_Menu_Option.Multiplayer: # when game_mode isn't Campaign
        game_session: tuple[bool, Board] = play_game(game_mode, game_board, players, secret_code) # play game
        display_board(game_session[1]) # final board display
        end_game(game_mode, current_stage, game_session[0], players, secret_code) # end of game

    elif game_mode == Main_Menu_Option.Campaign and campaign_flag == False: # when game mode is Campaign and CodeBreaker has lost
        end_game(game_mode, current_stage, campaign_flag, players, secret_code[current_stage]) # end of game

    elif game_mode == Main_Menu_Option.Campaign and campaign_flag == True: # when game mode is Campaign and CodeBreaker has not lost yet
        print(f"------------------------------------------------------------------ STAGE {current_stage+1} ------------------------------------------------------------------")
        game_stage: tuple[bool, Board] = play_game(game_mode, game_board[current_stage], players, secret_code[current_stage], 1, current_stage) # play game

        if game_stage[0] == False:
            display_board(game_stage[1])
            end_game(game_mode, current_stage, game_stage[0], players, secret_code[current_stage])

        else:
            if current_stage == 2:
                end_game(game_mode, current_stage, campaign_flag, players, secret_code[current_stage])
            else:
                end_game(game_mode, current_stage, game_stage[0], players, secret_code[current_stage])
                return start_gameplay(game_mode, game_board, players, secret_code, game_stage[0], current_stage+1)


def get_guess(guess_size: int = 1) -> Guess:
    """
    a recursive function that retrieves the Guess from the CodeBreaker's input

    Parameters:
        guess_size (int) - An indicator as to whether the Guess is the correct length or not

    Returns:
        Guess - The CodeBreaker's Guess
        
    """
    print(f"\n---------- CODE PEG CHOICE NO.#{guess_size} ----------")
    if guess_size == 4:
        return (receive_code_peg_input(),)
    else:
        return (receive_code_peg_input(),) + get_guess(guess_size+1)


def get_feedback(guess: Guess, secret: Secret) -> tuple[bool, Feedback]:
    """
    get_feedback assigns Red, White and Empty Hint pegs to the CodeBreaker's Guess, and decides whether the game has finished or not

    Parameters:
        guess (Guess) - The CodeBreaker's Guess
        secret (Secret) - The Secret code to Guess

    Returns:
        tuple[bool, Feedback] - The Boolean value indicating whether the game has finished or not, and the Feedback on the CodeBreaker's Guess
        
    """
    if guess == secret:
        return [True, tuple([Hint.Red] * 4)]
    else:
        red : list = get_red_hints(guess, secret) 
        white : list = get_white_hints(guess, secret, red) 
        feedback : list[Hint] = join_hints(red, white)
        final_feedback : Feedback = sort_hints(feedback) 
        return [False, final_feedback]


def join_hints(red_pegs : list, white_pegs : list) -> list[Hint]:
    """
    join_hints merges the lists of Red Hint pegs and White Hint pegs

    Parameters:
        red_pegs (list) - The list indicating which Code pegs should be assigned Red Hint pegs
        white_pegs (list) - The list indicating which Code pegs should be assigned White Hint pegs

    Returns:
        list[Hint] - A list of feedback
    
    """
    return list(map(lambda i: Hint.Red if red_pegs[i][0] else Hint.White if white_pegs[i][0] else Hint.Empty, range(4)))


def sort_hints(feedback: list[Hint]) -> Feedback: 
    """
    sort_hints sorts the list of Hints prioritising Red Hint pegs over White Hint pegs, and White Hint pegs over Empty Hint pegs

    Parameters:
        feedback (list[Hint]) - The unsorted list of feedback

    Returns:
        Feedback - The sorted Feedback
        
    """
    feedback_order = {Hint.Red: 0, Hint.White: 1, Hint.Empty: 2}
    return tuple(sorted(feedback, key=lambda x: feedback_order[x]))

 
def get_red_hints(guess: Guess, secret: Secret) -> list:
    """
    get_red_hints assigns Red Hint pegs or Empty Hint pegs to each Code peg in the CodeBreaker's Guess

    Parameters:
        guess (Guess) - The CodeBreaker's Guess
        secret (Secret) - The Secret to guess

    Returns:
        list - A list of tuples containing a Boolean and Code peg value to indicate whether
            a Red Hint peg or Empty Hint peg has been assigned to them
        
    """
    return [(True, guess[i]) if guess[i] == secret[i] else (False, guess[i]) for i in range(len(guess))]


def get_white_hints(guess : Guess, secret : Secret, red_pegs : list) -> list:
    """
    get_white_hints assigns White Hint pegs or Empty Hint pegs to each Code peg in the CodeBreaker's Guess

    Parameters:
        guess (Guess) - The CodeBreaker's Guess
        secret (Secret) - The Secret to guess
        red_pegs (list) - The list of red pegs assigned

    Returns:
        list - A list of tuples containing a Boolean and Code peg value to indicate whether
            a White Hint peg or Empty Hint peg has been assigned to them
        
    """

    # need to move out of function tomorrow --------------------------------------------------------------------
    def check_if_dupe(peg : Code, secret : Secret) -> bool: 
        """
        check_if_dupe checks whether the given peg is a duplicated peg in the Secret code or not

        Parameters:
            peg (Code) - The peg to check
            secret (Secret) - The Secret code

        Returns:
            bool - Whether the peg is a duplicated peg or not
            
        """
        return secret.count(peg) == 2


    def check_guessed_correctly(peg : Code, red_pegs : list) -> int: 
        """
        checks how many times a peg has been assigned a Red Hint peg 

        Parameters:
            peg (Code) - The peg to check
            red_pegs (list) - The list of Red Hint peg indicators

        Returns:
            int - The number of times the peg has been assigned a Red Hint peg
            
        """
        return red_pegs.count((True, peg))


    def check_almost_guessed(peg : Code, running_feedback : list) -> int:
        """
        checks how many times a peg has been assigned a White Hint peg

        Parameters:
            peg (Code) - The peg to check
            running_feedback (list) - The current list of White Hint peg indicators

        Returns:
            int - The number of times the peg has been assigned a White Hint peg
            
        """
        return running_feedback.count((True, peg))


    def occurs_once(peg : Code, red_pegs : list, running_feedback : list) -> tuple[bool, Code]:
        """
        occurs_once checks if a Code peg meets the criteria to be assigned a White Hint peg
            if it occurs only once in the Secret code

        Parameters:
            peg (Code) - The peg to check
            red_pegs (list) - The list of Red Hint peg indicators
            running_feedback (list) - The current list of White Hint peg indicators

        Returns:
            tuple[bool, Code] - A boolean value indicating whether the peg can be assigned 
                a White Hint peg or not, and the Code peg
            
        """
        return [(check_guessed_correctly(peg, red_pegs) == 0 and check_almost_guessed(peg, running_feedback) == 0), peg]


    def occurs_twice(peg : Code, red_pegs : list, running_feedback : list) -> tuple[bool, Code]:
        """
        checks if a Code peg meets the criteria to be assigned a White Hint peg if it is the duplicate peg in the Secret code

        Parameters:
            peg (Code) - The peg to check
            red_pegs (list) - The list of Red Hint peg indicators
            running_feedback (list) - The current list of White Hint peg indicators

        Returns:
            tuple[bool, Code] A boolean value indicating whether the peg can be assigned 
                a White Hint peg or not, and the Code peg
            
        """
        return [((check_guessed_correctly(peg, red_pegs) + check_almost_guessed(peg, running_feedback)) < 2), peg]

    def check_through_guess(guess_left: tuple, running_feedback : list) -> list:
        """
        a recursive function that assigns White Hint pegs for feedback

        Parameters:
            guess_left (tuple) - The remaining CodeBreaker's guess to check
            running_feedback (list) - The current list of White Hint peg indicators

        Returns:
            list - A list of tuples containing a Boolean and Code peg value to indicate whether
                a White Hint peg or Empty Hint peg has been assigned to them
                
        """
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
    # ---------------------------------------------------------------------------------------------------------------------------------------------------

    feedback : list = check_through_guess(guess, [])
    return feedback


def print_in_colour(peg: Union[Code, Hint]) -> str:
    """
    print_in_colour returns the string of a Code or Hint peg along with its ANSI escape code so it can be printed in colour

    Parameters:
        peg (Union[Code, Hint]) - The peg to print in colour

    Returns:
        str - The coloured peg string
        
    """
    match peg:
        case Code_Peg_Option.Orange:
            return "\033[38;5;208morange\033[0m"
        case Code_Peg_Option.Green:
            return "\033[38;5;82mgreen\033[0m"
        case Code_Peg_Option.Blue:
            return "\033[38;5;12mblue\033[0m"
        case Code_Peg_Option.Yellow:
            return "\033[38;5;184myellow\033[0m"
        case Code_Peg_Option.Purple:
            return "\033[38;5;134mpurple\033[0m"
        case Code_Peg_Option.Brown:
            return "\033[38;5;94mbrown\033[0m"
        case Code_Peg_Option.Empty:
            return "     "
        case Hint_Peg.White:
            return "\033[38;5;15mwhite\033[0m"
        case Hint_Peg.Red:
            return "\033[38;5;124mred\033[0m"
        case Hint_Peg.Empty:
            return "     "
           

def display_board(game_board: Board) -> None:
    """
    prints out the current game board

    Parameters:
        game_board (Board) - The game board to display

    """
    header : list[str] = [
        "DISPLAYING BOARD ---------------------------",
        "",
        " GUESS                                 FEEDBACK",
        " -------- -------- -------- --------   -------- -------- -------- -------- "
        ]

    board : list[str] = [format_row(row) for row in game_board]

    print("\n".join(header + board))


def format_row(row: Row) -> list[str]:
    """
    formats the Row of a Board

    Parameters:
        row (Row) - The Row to format

    Returns:
        list[str] - The formatted row
        
    """
    header : list[str] = ["|        |        |        |        | |        |        |        |        |"]

    guess: Guess = row[0]
    feedback: Feedback = row[1]

    row_pegs: list[str] = [format_peg(peg) for peg in guess] + ["| "] + [format_peg(peg) for peg in feedback] + ["|"]

    footer : list[str] = ["|        |        |        |        | |        |        |        |        |",
                    " -------- -------- -------- --------   -------- -------- -------- -------- "]

    return "\n".join(header) + "\n" + "".join(row_pegs) + "\n" + "\n".join(footer)


def format_peg(peg: Union[Code, Hint]) -> str:
    """
    formats a Code peg or Hint peg of a Row

    Parameters:
        peg (Union[Code, Hint]) - The Code peg or Hint peg to format

    Returns:
        str - The formatted peg
        
    """
    match len(str(peg)):
        case 6:
            return f"| {print_in_colour(peg)} "
        case _:
            padding: str = " " * (6-len(str(peg)))
            return f"| {print_in_colour(peg)}{padding} "


def update_board(game_board: Board, new_guess: Guess, new_feedback: Feedback, turn_count: int) -> Board:
    """
    updates the existing game board to contain the newly made Guess

    Parameters:
        game_board (Board) - the current state of the game board
        new_guess (Guess) - forms first portion of the tuple in new_row
        new_feedback (Feedback) - forms second portion of the tuple in new_row
        turn_count (int) - governs the position within the new Board to which new_row is updated in

    Returns:
        Board - an updated version of the Board is formed combining the existing Board and the new Row

    """
    new_row: Row = (new_guess, new_feedback)
    match len(game_board):
        case 6:# GOODBYE - jk
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
        case 4:
            match turn_count:
                case 1:
                    return (new_row, ) + game_board[:-1]
                case 2:
                    return game_board[:-3] + (new_row, ) + game_board[2:]
                case 3:
                    return game_board[:-2] + (new_row, ) + game_board[3:]
                case 4:
                    return game_board[0:3] + (new_row, )

def end_game(game_mode: Main_Menu_Option, current_stage: int, game_finished: bool, players: Players, secret: Secret) -> None:
    """
    end_game reveals the Secret code and the winner of the game

    Parameters:
        game_mode (Main_Menu_option) - Current game mode
        current_stage (int) - Current stage of Campaign if that is the game mode
        game_finished (bool) - Whether the game has ended or not
        players (tuple) - The pair of players playing the game
        secret (Secret) - The Secret code to reveal
    """
    print("\n---------- SECRET CODE ----------")
    print(*(print_in_colour(peg) for peg in secret))

    print("\n---------- FINAL RESULTS ----------")
    match game_finished:
        case True:
            print(f"\n{str(players[0])} has won the game!")
        case False:
            print(f"\n{str(players[1])} has won the game!")

    # if game_mode is Campaign
    if game_mode == Main_Menu_Option.Campaign and current_stage == 2 and game_finished == True:
        print("You have successfully completed your Campaign game!")
    elif game_mode == Main_Menu_Option.Campaign and current_stage < 2 and game_finished == True:
        print("Well done! You have advanced to the next stage in your Campaign game!")
    elif game_mode == Main_Menu_Option.Campaign and game_finished == False:
        print("You have failed your Campaign game!")


# ---------- Program Start Flow ----------
if __name__=="__main__":
    print(mastermind_intro) 

    while True:
        receive_main_menu_input()