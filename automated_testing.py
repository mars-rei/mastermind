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


# testing parse_code_peg_option - we should add .strip()
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


# testing format_row - need to work out -----------------------------------------------------------------------------------
def test_format_empty_row():
    row = ((Code_Peg_Option.Empty, Code_Peg_Option.Empty, Code_Peg_Option.Empty, Code_Peg_Option.Empty), (Hint_Peg.Empty, Hint_Peg.Empty, Hint_Peg.Empty, Hint_Peg.Empty))
    row_str = ""
    assert format_row(row) == row_str

def test_format_half_row():
    row = ((Code_Peg_Option.Empty, Code_Peg_Option.Empty, Code_Peg_Option.Empty, Code_Peg_Option.Empty), (Hint_Peg.Empty, Hint_Peg.Empty, Hint_Peg.Empty, Hint_Peg.Empty))
    row_str = ""
    assert format_row(row) == row_str

def test_format_full_row():
    row = ((Code_Peg_Option.Empty, Code_Peg_Option.Empty, Code_Peg_Option.Empty, Code_Peg_Option.Empty), (Hint_Peg.Empty, Hint_Peg.Empty, Hint_Peg.Empty, Hint_Peg.Empty))
    row_str = ""
    assert format_row(row) == row_str


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


# need to extra here
def test_end_campaign_game(capsys):
    end_game(Main_Menu_Option.Campaign, 1, True, (CodeBreaker(), CPU()), (Code_Peg_Option.Orange, Code_Peg_Option.Green, Code_Peg_Option.Blue, Code_Peg_Option.Purple))
    capture = capsys.readouterr()

    assert "\x1b[38;5;208morange\x1b[0m \x1b[38;5;82mgreen\x1b[0m \x1b[38;5;12mblue\x1b[0m \x1b[38;5;134mpurple\x1b[0m\n" in capture.out
    assert "\nCode Breaker has won the game!" in capture.out
    