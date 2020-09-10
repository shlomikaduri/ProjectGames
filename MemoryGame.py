import random,Utils,time,Score
'''
The purpose of memory game is to display an amount of random numbers to the users for 0.7
seconds and then prompt them from the user for the numbers that he remember.
If he was right with all the numbers the user will win otherwise he will lose.
'''

'''
get a number variable named difficulty
generate a list of random numbers between 1 to 101. The list length will be
difficulty.
The list will be shown for 0.7 seconds (using Utils.py module).
'''
def generate_sequence(difficulty):
    list_of_numbers =[]
    for i in range(difficulty):
        list_of_numbers.append(random.randint(1, 101))
    print("list_of_generated_numbers: "+ str(list_of_numbers))
    time.sleep(0.7)
    Utils.screen_cleaner()

    return(list_of_numbers)

'''
get a number variable named difficulty
prompt the user the following message:
After seeing the numbers enter the numbers you saw, each one separated with
Enter.
return a list of numbers prompted from the user. The list length will be in the size
of difficulty.
'''
def get_list_from_user(difficulty):
    list_from_user = []
    print("After seeing the numbers enter the numbers you saw, each one separated with Enter.")
    for i in range(difficulty):
        try:
            list_from_user.append(int(input()))
        except:
            print("wrong input format")
    print("list_from_user: " + str(list_from_user))
    return(list_from_user)


'''
get 2 variables named list_a and list_b
The function compare the two lists (list_a & list_b).
The function return True / False if the lists equal or not.
'''
def is_list_equal(list_a,list_b):
    if list_a==list_b:
        print("Win")
        return True
    else:
        print("Lose")
        return False


'''
get a number variable named difficulty
call the functions above and play the game.
return True / False if the user lost or won (based on is_list_equal()).
'''
def play(difficulty):
    if is_list_equal(generate_sequence(difficulty), get_list_from_user(difficulty))==True:
        Score.add_score(difficulty)
        return True
    else:
        return False



