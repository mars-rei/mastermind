Feature: Choosing a game option

  Scenario: Player selects 1st game option
    Given they have specified an argument of 1 to the command line
     When they confirm their choice of game option
     Then 'You have decided to play Mastermind against the CPU.' should be output
     And the game board is displayed
     And the command line prompts the code breaker for their guess