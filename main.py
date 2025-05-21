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

        """
        Main_Menu_Option.parse_main_menu_option is a function
            which parses an input string to a Main_Menu_Option value

        Parameters:
            cls (Type[Main_Menu_Option]) - The Main_Menu_Option to parse
            input (str) - An input string to try to parse into a Main_Menu_Option

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
        Confirmation_Option.parse_confirmation_option is a function
            which parses an input string to a Confirmation_Option value

        Parameters:
            cls (Type[Confirmation_Option]) - The Confirmation_Option to parse
            input (str) - An input string to parse into a Confirmation_Option

        Returns:
            Confirmation_Option - The parsed input
        """

        try:
            lower_confirmation_input: str = input.lower().strip() # chained pipelining
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
        Code_Peg_Options.parse_code_peg_option is a function
            which parses an input string to a Code_Peg_Option value

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
        Code_Peg_Option.__str__ returns the lowercase string representation of the Code_Peg_Option

        Returns:
            str - The lowercase representation of the Code_Peg_Option
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
        Hint_Peg.__str__ returns the lowercase string representation of the Hint_Peg

        Returns:
            str - The lowercase representation of the Hint_Peg
        """
        return self.name.lower()

Hint: TypeAlias = Hint_Peg


# ---------- Player Types ----------
@dataclass(eq=True, frozen=True)
class CodeMaker:
    def __str__(self) -> str:
        """
        CodeMaker.__str__ returns the string representation of CodeMaker

        Returns:
            str - The string representation of the CodeMaker
        """
        return "Code Maker"

@dataclass(eq=True, frozen=True)
class CodeBreaker:
    def __str__(self) -> str:
        """
        CodeBreaker.__str__ returns the string representation of CodeBreaker

        Returns:
            str - The string representation of the CodeBreaker
        """
        return "Code Breaker"

@dataclass(eq=True,frozen=True)
class CPU:
    def __str__(self) -> str:
        """
        CPU.__str__ returns the string representation of CPU

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
empty_normal_board: Normal_Board = (emptyRow, emptyRow, emptyRow, emptyRow, emptyRow, emptyRow) 


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
def check_one_dupe_pair_secret(secret_code: Secret, index_position: int = 0, found_dupe: tuple[Secret] = ()) -> bool:
    """
    check_one_dupe_pair_secret is a function
        that individually obtains the value from every index within
        secret_code whilst the found_dupe does not contain the 1st instance of
        a duplication pair.
        Using this, we can update found_dupe with the Code Peg found as the 1st
        instance of a duplication pair and return the appropriate bool

    Parameters:
        secret_code (Secret) - The newly created Secret Code to be guessed
        index_position (int) - Initially set to 0 but is overwritten by itself incremented by 1 for every recurse
        found_dupe (tuple[Secret]) - Initially empty but will soon store the 1st instance of a duplicate pair

    Returns:
        bool - To signify whether more than one duplicate pair has been found

    """
    
    if index_position == 4 and found_dupe:
        return False
    else:
        if secret_code.count(secret_code[index_position]) == 2 and secret_code[index_position] not in found_dupe:
            return check_one_dupe_pair_secret(secret_code, index_position+1, (secret_code[index_position], ) + found_dupe)
        elif secret_code.count(secret_code[index_position]) == 2 and found_dupe:
            return True

def check_two_dupe_secret(secret_code: Secret, index_position: int = 0) -> bool:
    """
    check_two_dupe_secret is a function
        that individually obtains the value from every index within
        secret_code and counts the amount of appearances within secret_code.
        Using this, it decides whether or not to recurse or return the
        appropriate bool.


    Parameters:
        secret_code (Secret) - The newly created Secret Code to be guessed
        index_position (int) - Initially set to 0 but is overwritten by itself incremented by 1 for every recurse

    Returns:
        bool - To signify whether any of the code pegs selected appear more than twice

    """
        
    if index_position == 4:
        return False
    else:
        if secret_code.count(secret_code[index_position]) <= 2:
            return check_two_dupe_secret(secret_code, index_position+1)
        elif secret_code.count(secret_code[index_position]) >= 3:
            return True


def receive_main_menu_input() -> None: # TODO

    """
    receive_main_menu_input is a function
        which receives the user's parsed Main_Menu_Option and 
        based on this, calls the appropriate main menu option function
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
            # TODO - Document/Create start_campaign Function
            start_gameplay(selected_option, (normal_secret_code, hard_secret_code), (CodeBreaker(), CPU()), (normal_secret_code(), hard_secret_code(), hard_secret_code()))
        case Main_Menu_Option.Exit:
            print("Exiting Mastermind...")
            sys.exit()


def receive_code_peg_input() -> Code: 

    """
    receive_code_peg_input is a function
        which receives the user's parsed Code_Peg_Option and 
        based on this, print out the appropriate message to 
        the command-line

    Returns:
        Code - The Player's selected option
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


def receive_confirmation_input(tupleInput: Union[Guess, Secret]) -> Confirmation_Option: # TO DO - change return to Boolean?

    """
    receive_confirmation_input is a function
        which receives the user's parsed Confirm_Option and 
        based on this, it prints out the appropriate message to
        the command-line

    Parameters:

    Returns:
        
    """

    while True:
        print("\nYour Guess: ") # would rather substitute Guess with Choice so it would make sense when used for makeSecretCode too
        print(*(print_in_colour(peg) for peg in tupleInput))
        print("Are you sure you want to continue?") 
        selected_option = Confirmation_Option.parse_confirmation_option(input("> "))
        print()

        match selected_option:
            case Confirmation_Option.Yes:
                print("\nGuess Confirmed.") # would rather substitute Guess with Choice so it would make sense when used for makeSecretCode too
                return True
            case Confirmation_Option.No:
                print("\nGuess Cancelled.") # would rather substitute Guess with Choice so it would make sense when used for makeSecretCode too
                return False
  

def normal_secret_code() -> Secret: 
    """
    normal_secret_code generates a normal Secret code to be guessed by the CodeBreaker

    Returns:
        Secret - A Secret code made up of 4 unique Code pegs
        
    """
    valid_code_pegs: list[Code] = [peg for peg in Code if str(peg) != "empty"]
    newSecretCode: Secret = tuple(random.sample(valid_code_pegs, k=4))
    return newSecretCode


def make_secret_code(secret_size: int = 1) -> Secret: # TODO
    """
    make_secret_code is a function
        that prompts for each individual Code Peg input to return a Secret.
        Until secret_size is of value 4, receive_code_peg_input will be called
        without recurse to return a formulated Secret. 

    Parameters:
        secret_size (int) - Initially value 1 and is overwritten byt itself incremented by 1 when recursed

    Returns:
        Secret - Tuple containing the selected four Code type values
    
    """
    print()
    print(f"---------- CODE PEG CHOICE NO.#{secret_size} ----------")
    if secret_size == 4:
        return (receive_code_peg_input(),)
    else:
        return (receive_code_peg_input(),) + get_guess(secret_size+1)


def hard_secret_code() -> Secret: 
    """
    hard_secret_code generates a hard Secret code to be guessed by the CodeBreaker

    Returns:
        Secret - A Secret code made up of 2 unique Code pegs and a pair of duplicate Code pegs
        
    """
    valid_code_pegs: list[Code] = [peg for peg in Code if peg != Code(0)]
    no_duplicate_sample: list[Code] = random.sample(valid_code_pegs, k=3)
    duplicate_code: list[Code] = no_duplicate_sample + [no_duplicate_sample[2]]
    newSecretCode: Secret = tuple(random.sample(duplicate_code, k=4))
    return newSecretCode 


# ----------------------------------------------------------------------------------------------------------------------------------------------------------

# IN-PROGRESS function
def play_round(game_board: Board, secret_code: Secret, turn_count: int) -> tuple[Board, bool]:    
    """
    play_round is a function
        that executes a sequence of functions to carry out a singular
        guess. This involves the prompt for the Guess, the Confirmation_Option,
        the Feedback generated, and updating the Board.

    Parameters:
        game_board (Board) - To be manipulated to create a new updated version for a Board value
        secret_code (Secret) - To be passed into get_feedback() to be compared with new_guess
        turn_count (int) - To be passed into update_board() to govern what Row of the Board is to be updated

    Returns:
        tuple[Board, bool] - Returns the newly updated_board alongside the finished status of the game as a bool

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


# IN-PROGRESS function
def play_game(game_board: Board, players: tuple[Player, Player], secret_code: Secret, turn_count: int = 1, game_finished: bool = False) -> tuple[bool, Board]:
    """
    play_game is a function
        that regulates the amount of attempts that a singular
        Mastermind Game Mode can be taken. While turn_count
        or game_finished have not meant a certain criteria to
        end the game session, play round is called to allow for
        an attempt to be made and a recurse is made.

    Parameters:
        game_board (Board) - To be passed into play_round()
        players (tuple[Player, Player]) - To be passed into the play_game() recursive call
        secret_code (Secret) - To be passed into play_round() and the play_game() recursive call
        turn_count (int) - Initialised as 1 and passed into the play_game() recursive call incremented by 1
        game_finished (bool) - Initialsied as False and governs the end of the game session.

    Returns:
        tuple[bool, Board] - Returns the finished state of the game indicating the winner and the final state of the Board
        
    """
    if turn_count == 7 or game_finished == True:
        return (game_finished, game_board)
    else:
        print(f"\n---------- GUESS ATTEMPT NO.#{turn_count} ----------")
        round: tuple[Board, bool] = play_round(game_board, secret_code, turn_count)
        return play_game(round[0], players, secret_code, turn_count+1, round[1])


# IN-PROGRESS function (GELO is thinking of putting recursion here for campaign exclusively)
def start_gameplay(game_mode: Main_Menu_Option, game_board: Board, players: tuple[Player, Player], secret_code: Union[Secret, tuple[Secret, Secret, Secret]]) -> None:
    """
    start_gameplay is a function
        that displays the game mode chosen and decides on the flow
        in which the a certain game mode should behave in.
        Depending on which game mode is chosen will govern the
        amount of play_game() calls will be made until the a final
        end_game() call is made.

    Parameters:
        game_mode (Main_Menu_Option) - Used to govern the which flow of the gameplay
        game_board (Board) - To pass the appropriate Board into the first instance of a play_game() call
        players (tuple[Player, Player]) - To pass the appropriate tuple of players into the first instance of a play_game() call
        secret_code (Secret or tuple[Secret, Secret, Secret]) - To be passed, or individually passed if in a tuple, into the first instance of a play_game() call

    Returns:
        None
        
    """
    print(f"""
                                            _______________
    ----------------------------------------| {game_mode.name.upper()} |----------------------------------------
    ----------------------------------------|   GAME MODE   |----------------------------------------
    ----------------------------------------|_______________|----------------------------------------
            """)
    if game_mode == Main_Menu_Option.Single_Player or game_mode == Main_Menu_Option.Multiplayer:    
        game_session: tuple[bool, Board] = play_game(game_board, players, secret_code)
        display_board(game_session[1])
        end_game(game_session[0], players, secret_code)
    if game_mode == Main_Menu_Option.Campaign:
        pass
        stage_one: tuple[bool, Board] = play_game()

# ----------------------------------------------------------------------------------------------------------------------------------------------------------


def get_guess(guess_size: int = 1) -> Guess:
    """
    get_guess is a recursive function that retrieves the Guess from the CodeBreaker's input

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
    get_feedback assigns Red, White and Empty Hint pegs to the CodeBreaker's Guess,
        creating Feedback and decides whether the Mastermind game has finished or not

    Parameters:
        guess (Guess) - The CodeBreaker's Guess
        secret (Secret) - The Secret code to Guess

    Returns:
        tuple[bool, Feedback] - The Boolean value indicating whether the game has finished or not,
        and the Feedback on the CodeBreaker's Guess
        
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
    join_hints merges the list of Red Hint pegs and White Hint pegs in order to
        create Feedback

    Parameters:
        red_pegs (list) - The list indicating which Code pegs should be assigned Red Hint pegs
        white_pegs (list) - The list indicating which Code pegs should be assigned White Hint pegs

    Returns:
        list[Hint] - The unsorted list of feedback
    
    """
    return list(map(lambda i: Hint.Red if red_pegs[i][0] else Hint.White if white_pegs[i][0] else Hint.Empty, range(4)))


def sort_hints(feedback: list[Hint]) -> Feedback: 
    """
    sort_hints sorts the list of Hints prioritising Red Hint pegs over White Hint pegs,
        and White Hint pegs over Empty Hint pegs

    Parameters:
        feedback (list[Hint]) - The unsorted list of feedback

    Returns:
        Feedback - The sorted Feedback
        
    """
    feedback_order = {Hint.Red: 0, Hint.White: 1, Hint.Empty: 2}
    return tuple(sorted(feedback, key=lambda x: feedback_order[x]))

 
def get_red_hints(guess: Guess, secret: Secret) -> list:
    """
    get_red_hints assigns Red Hint pegs or Empty Hint pegs to each Code peg in the 
        CodeBreaker's Guess

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
    get_white_hints assigns White Hint pegs or Empty Hint pegs to each Code peg in the 
        CodeBreaker's Guess

    Parameters:
        guess (Guess) - The CodeBreaker's Guess
        secret (Secret) - The Secret to guess
        red_pegs (list) - The list of red pegs assigned

    Returns:
        list - A list of tuples containing a Boolean and Code peg value to indicate whether
            a White Hint peg or Empty Hint peg has been assigned to them
        
    """

    def check_if_dupe(peg : Code, secret : Secret) -> bool: 
        """
        check_if_dupe checks whether the given peg is a duplicated peg in the Secret
            code or not

        Parameters:
            peg (Code) - The peg to check
            secret (Secret) - The Secret code

        Returns:
            bool - Whether the peg is a duplicated peg or not
            
        """
        return secret.count(peg) == 2
    

    def check_guessed_correctly(peg : Code, red_pegs : list) -> int: 
        """
        check_guessed_correctly checks how many times a peg has been correctly matched
            (has been assigned a Red Hint peg already)

        Parameters:
            peg (Code) - The peg to check
            red_pegs (list) - The list of Red Hint peg indicators

        Returns:
            int - The number of times the peg has been assigned a Red Hint peg
            
        """
        return red_pegs.count((True, peg))
    

    def check_almost_guessed(peg : Code, running_feedback : list) -> int:
        """
        check_almost_guessed checks how many times a peg has been almost matched
            (has been assigned a White Hint peg already)

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
        occurs_twice checks if a Code peg meets the criteria to be assigned a White Hint peg
            if it is the duplicate peg in the Secret code

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
        check_through_guess is a recursive function that assigns White Hint pegs for feedback

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


    feedback : list = check_through_guess(guess, [])
    return feedback


def print_in_colour(peg: Union[Code, Hint]) -> str:
    """
    print_in_colour returns the string of a Code or Hint peg along with its ANSI escape code
        so it can be printed in its corresponding colour

    Parameters:
        peg (Union[Code, Hint]) - The peg to print in colour

    Returns:
        str - The peg along with its colour to be printed
        
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
    display_board prints out the current game board

    Parameters:
        game_board (Board) - The game board to display

    """

    def format_row(row: Row) -> list[str]:
        """
        format_row formats the Row of a Board

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
        format_peg formats a Code peg or Hint peg of a Row

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
            

    header : list[str] = [
        "DISPLAYING BOARD ---------------------------",
        "",
        " GUESS                                 FEEDBACK",
        " -------- -------- -------- --------   -------- -------- -------- -------- "
        ]

    board : list[str] = [format_row(row) for row in game_board]

    print("\n".join(header + board))


def update_board(game_board: Board, new_guess: Guess, new_feedback: Feedback, turn_count: int) -> Board:
    """
    update_board is a function
        that uses the existing game board and updates it appropriately
        with a new Row containing the new_guess and new_feedback.

    Parameters:
        game_board (Board) - To updated through tuple slicing along with new_row
        new_guess (Guess) - Forms part of the Row tuple in new_row
        new_feedback (Feedback) - Forms art fo the Row tuple in new_row
        turn_count (int) - Governs the position within the new Board to which new_row is updated

    Returns:
        Board - An updated version of the Board is formed combining the existing Board and the new Row

    """
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


def end_game(game_finished: bool, players: Players, secret: Secret) -> None:
    """
    end_game reveals the Secret code and the winner of the Mastermind game

    Parameters:
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


# ---------- Program Start Flow ----------
if __name__=="__main__":
    print(mastermind_intro) 

    while True:
        receive_main_menu_input()