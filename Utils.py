import os,time
'''
This file will contain general information and operations we need for our game.
'''

SCORES_FILE_NAME = "Scores.txt"
ERROR_MESSAGE = "Something went wrong.."
BAD_RETURN_CODE = "File not found"

'''
A function to clear the screen
'''
def screen_cleaner():
    os.system('cls' if os.name == 'nt' else 'clear')

