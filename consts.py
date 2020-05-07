"""
Constants for the game

This module contains global constants for the game. As these are spread
across multiple modules, we separate the constants into their own module. This
allows all modules to access them.
"""

### MATCH CONSTANTS ###

#: match was created but game has not started
MATCH_INIT = 0

#: the game is being played
MATCH_ACTIVE = 1

#: the game has been finished, and a winner decided
MATCH_DONE = 2
