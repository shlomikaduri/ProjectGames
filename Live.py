import MemoryGame,GuessGame
'''
This function print Hello to the user - name
'''
def welcome(name):
    print("Hello " + name + " and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")


'''
print out the following text:
Please choose a game to play:
1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back
2. Guess Game - guess a number and see if you chose like the computer

get user input : game and difficulty chooses
'''

def load_game():
    print("\nPlease choose a game to play:\n1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n2. Guess Game - guess a number and see if you chose like the computer")
    try:
        user_choose = int(input())
    except:
        print("Please enter valid game number")

    while user_choose!=1 and user_choose!=2:
        print("Please enter game number - only 1 or 2")
        user_choose = int(input())
        if user_choose==1 or user_choose==2:
            break
    print("Please choose game difficulty from 1 to 5:")
    difficulty_choose = int(input())
    while difficulty_choose<1 or difficulty_choose>5:
        print("Please choose game difficulty from 1 to 5")
        difficulty_choose = int(input())
        if difficulty_choose>=1 and difficulty_choose<=5:
            print("break")
            break

    if(user_choose==1):
        if(MemoryGame.play(difficulty_choose)==True):
            return True
        else:
            return False
    elif (user_choose==2):
        if(GuessGame.play(difficulty_choose)==True):
            return True
        else:
            return False
    else:
        print("error chooses")





