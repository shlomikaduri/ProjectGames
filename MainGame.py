'''
The purpose of this main is to load the game select menu, load the selected game and difficulty, run the game, update score and return the status, win or lose.
'''

from Live import load_game, welcome


if __name__ == '__main__':
    print(welcome("Daniel"))  # user name and welcome message
    while (True):
        if (
                load_game() == True):  # if the user won the game. the program will be ginshed, if the user lose, contniues running.
            break