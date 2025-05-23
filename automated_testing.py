import pytest
from main import *

# testing parse_main_menu_option
def test_parse_main_menu_option():
    assert Main_Menu_Option.parse_main_menu_option("1") == Main_Menu_Option.Single_Player
    assert Main_Menu_Option.parse_main_menu_option("2") == Main_Menu_Option.Multiplayer
    assert Main_Menu_Option.parse_main_menu_option("3") == Main_Menu_Option.Campaign
    assert Main_Menu_Option.parse_main_menu_option("4") == Main_Menu_Option.Exit
    assert Main_Menu_Option.parse_main_menu_option("") is None
    assert Main_Menu_Option.parse_main_menu_option("single player") is None


# testing parse_confirmation_option
def test_parse_confirmation_option():
    assert Confirmation_Option.parse_confirmation_option("Y") == Confirmation_Option.Yes
    assert Confirmation_Option.parse_confirmation_option("y ") == Confirmation_Option.Yes
    assert Confirmation_Option.parse_confirmation_option("YeS") is None
    assert Confirmation_Option.parse_confirmation_option("    N") == Confirmation_Option.No
    assert Confirmation_Option.parse_confirmation_option("n") == Confirmation_Option.No
    assert Confirmation_Option.parse_confirmation_option("no") is None
    assert Confirmation_Option.parse_confirmation_option("hell naur") is None
    assert Confirmation_Option.parse_confirmation_option("") is None


# testing parse_code_peg_option
def test_parse_code_peg_option():
    assert Code_Peg_Option.parse_code_peg_option("0") is None
    assert Code_Peg_Option.parse_code_peg_option("1") == Code_Peg_Option.Orange
    assert Code_Peg_Option.parse_code_peg_option("2") == Code_Peg_Option.Green
    assert Code_Peg_Option.parse_code_peg_option("3") == Code_Peg_Option.Blue
    assert Code_Peg_Option.parse_code_peg_option("4") == Code_Peg_Option.Yellow
    assert Code_Peg_Option.parse_code_peg_option("5") == Code_Peg_Option.Purple
    assert Code_Peg_Option.parse_code_peg_option("6") == Code_Peg_Option.Brown
    assert Code_Peg_Option.parse_code_peg_option("Orange") is None
    assert Code_Peg_Option.parse_code_peg_option("") is None


# testing Code_Peg_Option.__str__
def test_code_peg_option_str():
    assert str(Code_Peg_Option.Empty) == "empty"
    assert str(Code_Peg_Option.Orange) == "orange"
    assert str(Code_Peg_Option.Green) == "green"
    assert str(Code_Peg_Option.Blue) == "blue"
    assert str(Code_Peg_Option.Yellow) == "yellow"
    assert str(Code_Peg_Option.Purple) == "purple"
    assert str(Code_Peg_Option.Brown) == "brown"


# testing Hint_Peg.__str__
def test_hint_peg_str():
    assert str(Hint_Peg.Empty) == "empty"
    assert str(Hint_Peg.White) == "white"
    assert str(Hint_Peg.Red) == "red"


# testing get_feedback
def test_get_feedback():
    guess = (Code_Peg_Option.Green, Code_Peg_Option.Brown, Code_Peg_Option.Orange, Code_Peg_Option.Orange)
    secret = (Code_Peg_Option.Green, Code_Peg_Option.Brown, Code_Peg_Option.Orange, Code_Peg_Option.Orange)
    assert get_feedback(guess, secret) == [True, (Hint_Peg.Red, Hint_Peg.Red, Hint_Peg.Red, Hint_Peg.Red)]

    guess = (Code_Peg_Option.Green, Code_Peg_Option.Brown, Code_Peg_Option.Orange, Code_Peg_Option.Orange)
    secret = (Code_Peg_Option.Orange, Code_Peg_Option.Orange, Code_Peg_Option.Green, Code_Peg_Option.Brown)
    assert get_feedback(guess, secret) == [False, (Hint_Peg.White, Hint_Peg.White, Hint_Peg.White, Hint_Peg.White)]

    guess = (Code_Peg_Option.Green, Code_Peg_Option.Brown, Code_Peg_Option.Orange, Code_Peg_Option.Orange)
    secret = (Code_Peg_Option.Green, Code_Peg_Option.Orange, Code_Peg_Option.Green, Code_Peg_Option.Brown)
    assert get_feedback(guess, secret) == [False, (Hint_Peg.Red, Hint_Peg.White, Hint_Peg.White, Hint_Peg.Empty)] # logic is working incorrectly


# testing join_hints
def test_join_hints():
    red_pegs = [(False, Code_Peg_Option.Green), (True, Code_Peg_Option.Brown), (False, Code_Peg_Option.Orange), (False, Code_Peg_Option.Orange)]
    white_pegs = [(True, Code_Peg_Option.Green), (False, Code_Peg_Option.Brown), (True, Code_Peg_Option.Orange), (False, Code_Peg_Option.Orange)]
    assert join_hints(red_pegs, white_pegs) == [Hint_Peg.White, Hint_Peg.Red, Hint_Peg.White, Hint_Peg.Empty]


# testing sort_hints
def test_sort_hints():
    hints = [Hint_Peg.Empty, Hint_Peg.White, Hint_Peg.Red, Hint_Peg.Red]
    assert sort_hints(hints) == (Hint_Peg.Red, Hint_Peg.Red, Hint_Peg.White, Hint_Peg.Empty)


# testing get_red_hints
def test_get_red_hints():
    guess = (Code_Peg_Option.Green, Code_Peg_Option.Brown, Code_Peg_Option.Orange, Code_Peg_Option.Orange)
    secret = (Code_Peg_Option.Green, Code_Peg_Option.Brown, Code_Peg_Option.Orange, Code_Peg_Option.Orange)
    assert get_red_hints(guess, secret) == [(True, Code_Peg_Option.Green), (True, Code_Peg_Option.Brown), (True, Code_Peg_Option.Orange), (True, Code_Peg_Option.Orange)]

    guess = (Code_Peg_Option.Purple, Code_Peg_Option.Yellow, Code_Peg_Option.Orange, Code_Peg_Option.Orange)
    assert get_red_hints(guess, secret) == [(False, Code_Peg_Option.Purple), (False, Code_Peg_Option.Yellow), (True, Code_Peg_Option.Orange), (True, Code_Peg_Option.Orange)]


# testing check_if_dupe
def test_check_if_dupe():
    secret = (Code_Peg_Option.Green, Code_Peg_Option.Brown, Code_Peg_Option.Orange, Code_Peg_Option.Orange)
    assert check_if_dupe(Code_Peg_Option.Orange, secret) == True
    assert check_if_dupe(Code_Peg_Option.Green, secret) == False


# testing check_guessed_correctly
def test_check_almost_guessed_0():
    red_pegs = [(True, Code_Peg_Option.Orange)]
    assert check_almost_guessed(Code_Peg_Option.Green, red_pegs) == 0

def test_check_almost_guessed_1():
    red_pegs = [(True, Code_Peg_Option.Green), (True, Code_Peg_Option.Orange)]
    assert check_almost_guessed(Code_Peg_Option.Orange, red_pegs) == 1

def test_check_almost_guessed_2():
    red_pegs = [(True, Code_Peg_Option.Green), (True, Code_Peg_Option.Orange), (True, Code_Peg_Option.Blue), (True, Code_Peg_Option.Orange)]
    assert check_almost_guessed(Code_Peg_Option.Orange, red_pegs) == 2


# testing check_almost_guessed
def test_check_almost_guessed_0():
    running_feedback = [(True, Code_Peg_Option.Orange)]
    assert check_almost_guessed(Code_Peg_Option.Green, running_feedback) == 0

def test_check_almost_guessed_1():
    running_feedback = [(True, Code_Peg_Option.Green), (True, Code_Peg_Option.Orange)]
    assert check_almost_guessed(Code_Peg_Option.Orange, running_feedback) == 1

def test_check_almost_guessed_2():
    running_feedback = [(True, Code_Peg_Option.Green), (True, Code_Peg_Option.Orange), (True, Code_Peg_Option.Blue), (True, Code_Peg_Option.Orange)]
    assert check_almost_guessed(Code_Peg_Option.Orange, running_feedback) == 2


# testing the Player .__str__ functions
def test_code_maker_str():
    assert str(CodeMaker()) == "Code Maker"

def test_code_breaker_str():
    assert str(CodeBreaker()) == "Code Breaker"

def test_cpu_str():
    assert str(CPU()) == "CPU"


# test if normal_secret_code provides a tuple of distinct values
def test_normal_secret_code():
    code = normal_secret_code()
    assert len(code) == len(set(code))


# test if hard_secret_code provides a tuple of 2 distinct values and a pair of the same value
def test_hard_secret_code():
    code = hard_secret_code()
    assert len(set(code)) == 3


# testing format_peg
def test_format_peg():
    assert format_peg(Code_Peg_Option.Empty) == "|        "
    assert format_peg(Code_Peg_Option.Orange) == "| \x1b[38;5;208morange\x1b[0m "
    assert format_peg(Code_Peg_Option.Green) == "| \033[38;5;82mgreen\033[0m  "
    assert format_peg(Code_Peg_Option.Blue) == "| \033[38;5;12mblue\033[0m   "
    assert format_peg(Code_Peg_Option.Yellow) == "| \033[38;5;184myellow\033[0m "
    assert format_peg(Code_Peg_Option.Purple) == "| \033[38;5;134mpurple\033[0m "
    assert format_peg(Code_Peg_Option.Brown) == "| \033[38;5;94mbrown\033[0m  "
    assert format_peg(Hint_Peg.Empty) == "|        "
    assert format_peg(Hint_Peg.White) == "| \033[38;5;15mwhite\033[0m  "
    assert format_peg(Hint_Peg.Red) == "| \033[38;5;124mred\033[0m    "


# test end_game
# found capsys from yusuf's report
def test_end_single_player_game(capsys):
    end_game(Main_Menu_Option.Single_Player, None, False, (CodeBreaker(), CPU()), (Code_Peg_Option.Orange, Code_Peg_Option.Green, Code_Peg_Option.Blue, Code_Peg_Option.Purple))
    capture = capsys.readouterr()

    assert "\x1b[38;5;208morange\x1b[0m \x1b[38;5;82mgreen\x1b[0m \x1b[38;5;12mblue\x1b[0m \x1b[38;5;134mpurple\x1b[0m\n" in capture.out
    assert "\nCPU has won the game!" in capture.out

def test_end_multiplayer_game(capsys):
    end_game(Main_Menu_Option.Multiplayer, None, False, (CodeBreaker(), CodeMaker()), (Code_Peg_Option.Orange, Code_Peg_Option.Green, Code_Peg_Option.Blue, Code_Peg_Option.Purple))
    capture = capsys.readouterr()

    assert "\x1b[38;5;208morange\x1b[0m \x1b[38;5;82mgreen\x1b[0m \x1b[38;5;12mblue\x1b[0m \x1b[38;5;134mpurple\x1b[0m\n" in capture.out
    assert "\nCode Maker has won the game!" in capture.out


# for campaign message 1
def test_end_campaign_game(capsys):
    end_game(Main_Menu_Option.Campaign, 1, True, (CodeBreaker(), CPU()), (Code_Peg_Option.Orange, Code_Peg_Option.Green, Code_Peg_Option.Blue, Code_Peg_Option.Purple))
    capture = capsys.readouterr()

    assert "\x1b[38;5;208morange\x1b[0m \x1b[38;5;82mgreen\x1b[0m \x1b[38;5;12mblue\x1b[0m \x1b[38;5;134mpurple\x1b[0m\n" in capture.out
    assert "\nCode Breaker has won the game!" in capture.out
    assert "\nYou have successfully completed your Campaign game!" in capture.out

# for campaign message 2
def test_end_campaign_game(capsys):
    end_game(Main_Menu_Option.Campaign, 2, True, (CodeBreaker(), CPU()), (Code_Peg_Option.Orange, Code_Peg_Option.Green, Code_Peg_Option.Blue, Code_Peg_Option.Purple))
    capture = capsys.readouterr()

    assert "\x1b[38;5;208morange\x1b[0m \x1b[38;5;82mgreen\x1b[0m \x1b[38;5;12mblue\x1b[0m \x1b[38;5;134mpurple\x1b[0m\n" in capture.out
    assert "\nCode Breaker has won the game!" in capture.out
    assert "\nWell done! You have advanced to the next stage in your Campaign game!" in capture.out

# for campaign message 3
def test_end_campaign_game(capsys):
    end_game(Main_Menu_Option.Campaign, 1, False, (CodeBreaker(), CPU()), (Code_Peg_Option.Orange, Code_Peg_Option.Green, Code_Peg_Option.Blue, Code_Peg_Option.Purple))
    capture = capsys.readouterr()

    assert "\x1b[38;5;208morange\x1b[0m \x1b[38;5;82mgreen\x1b[0m \x1b[38;5;12mblue\x1b[0m \x1b[38;5;134mpurple\x1b[0m\n" in capture.out
    assert "\nCPU has won the game!" in capture.out
    assert "\nYou have failed your Campaign game!" in capture.out