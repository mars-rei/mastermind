# Mastermind Command-Line Game in Python 

## Project Aim
To create a small-scale prototype for the Mastermind game where it will take the form of an interactive command line program. 

The program must have the following features:
- allow a player to start a new 2-player game between a human codemaker and a human codebreaker
- allow a player to start a new single-player game against the CPU where the CPU is the code maker and
the code to break is algorithmically generated
- allow a player to start a new single-player ‘campaign’ against the CPU where the CPU acts as the code
maker but the codes are already predefined (acting as separate “levels” of the game)

The aim is to program this in the declarative programming paradigm.


## Contributors
- <ins>Imogen Dicen</ins>
  - [LinkedIn](https://www.linkedin.com/in/imogen-dicen/)
  - [Portfolio](https://reminiscent-flannel-fe7.notion.site/my-projects-0cd061a938b0467d98cb56019a970f6d?pvs=4)
- <ins>Angelo Luis Lagdameo</ins>
  - [LinkedIn](https://www.linkedin.com/in/angelo-luis-lagdameo)
  - [Portfolio](https://www.notion.so/Angelo-Luis-Lagdameo-1fec27bb36fd808185d2c8a27c1ce08b?source=copy_link)


## Other Project Details
<b>Project duration:</b> started in March 2025 and was submit in May 2025

<b>Project purpose:</b> developed for a university assignment for Computer Mathematics and Declarative Programming

<b>Level of completion:</b> completed (with a known logic error and a need of refactoring for paradigm consistency)


## Running the Program
<ins>__Prerequisites:__</ins>
1. Download the latest version of [Python](https://www.python.org/downloads/)
2. Download [main.py](https://github.com/mars-rei/mastermind/blob/main/main.py) from this repository

- <ins>__OPTION 1__</ins>
  - Right-click main.py and open with Python
- <ins>__OPTION 2__</ins>
  - Open Terminal and enter the command ```python main.py```
- <ins>__OPTION 3__</ins>
  - Run in your preferred IDE


## Areas for Improvement 
__[main.py](https://github.com/mars-rei/mastermind/blob/main/main.py)__
- Ensure all methods called within get_white_hints work as expected (this is where the logic error lies)
- Ensure most methods are of the declarative and functional programming styles
- Create a single function that would output to the terminal, updating all other methods that do to return strings to be output instead

__[automated_testing.py](https://github.com/mars-rei/mastermind/blob/main/automated_testing.py)__
- Fix single occurence of failed unit test
- Collaboratively devise any additional unit tests for functions not covered already

__Devise behavioural tests using [behave](https://behave.readthedocs.io/en/latest/) framework__

