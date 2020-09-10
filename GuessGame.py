import random,Score
'''
The purpose of guess game is to start a new game, cast a random number between 1 to a
variable called difficulty.
'''

'''
get a number variable named difficulty
return a random number between 1 to difficulty.
'''
def generate_number(difficulty):
    return(random.randint(1, int(difficulty)))



'''
get a number variable named difficulty
ask the user to guess a number between 1 to difficulty and return the number the
user guessed.
'''
def get_guess_from_user(difficulty):
    return(int(input("Please guess number from 1 to "+ difficulty)))


'''
get 2 variables: number variable named difficulty number variable named
secret_number
compare the secret generated number to the one prompted by the
get_guess_from_user.
'''
def compare_results(difficulty):
    guessed_number = get_guess_from_user(difficulty)
    secret_number = generate_number(difficulty)
    print("guessed_number is: "+ str(guessed_number))
    print("secret_number is: "+ str(secret_number))
    if guessed_number==secret_number:
        print("Win")
        return True
    else:
        print("Lose")
        return False



'''
get a number variable named difficulty
call the functions above and play the game.
return True / False if the user lost or won.
'''
def play(difficulty):
    if compare_results(str(difficulty))==True:
        Score.add_score(difficulty)
        return True
    else:
        return False







