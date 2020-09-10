import Utils
import pathlib

'''
A file which will manage the scores file.
The scores file at this point will consist of only a number.
That number is the accumulation of the winnings of the user.

Amount of points for winning a game is = 1 point per difficulty level (difficulty 3 = 3 points).
Each time the user is winning a game, the points he won will be added to his current amount of
point saved in a file.
'''

'''
A. The functions input is a variable called points.
B. The function will try to read the current score in the scores file, if it fails it will create a
new one and will use it to save the current score.
C. The function will print the user current score.
'''
def add_score(points):
    current_score=0
    try:
        file = pathlib.Path(Utils.SCORES_FILE_NAME)
        if file.exists():
            print ("File exist")
        else:
            print ("File not exist")
            score_file = open(Utils.SCORES_FILE_NAME, "w+")
            score_file.write("0")
            score_file.close()

    except IOError:
        print("error IOFile ")

    try:
        score_file = open(Utils.SCORES_FILE_NAME, "r")
        current_score = score_file.read()
        if len(str(current_score))>1:
            current_score= int(current_score)+points
        else:
            current_score=points
        score_file.close()

        score_file = open(Utils.SCORES_FILE_NAME, "w")
        score_file.write(str(current_score))
        score_file.close()
        print("user current score is: "+str(current_score))
    except IOError:
        print("error IOError file not exist")


