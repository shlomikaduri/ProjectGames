from selenium import webdriver

from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

'''
This file will have two functions.

1. test_scores_service(app_url) – Will test our web service.
Will get the application URL as an input, open a browser to that URL, select the score
element in our web page, check that it is a number between 0 to 1000 and return a
boolean value if it’s true or not.

2. main_function() –
Will call our tests function.
The main function will return -1 as an OS exit code if the tests failed and 0 if it passed.
'''
PORT_NUM = "5000"

def scores_test_service(app_url):
    try:
        driver = webdriver.Chrome(executable_path=r'C:\ProjectGames\chromedriver_win32\chromedriver.exe')
    except:
        print("------------ Error : please check chromedriver location \n\r Required to be locted at C:\ProjectGames\chromedriver_win32\chromedriver.exe ------------------")


    driver.implicitly_wait(10)
    driver.get(app_url)
    print(driver.title)

    try:
        score = driver.find_element_by_id("score")
        print(score.text)
    except:
        print(
            "------------ Error : please check chromedriver location \n\r ------------------")
        return False

    if int(score.text)>=0 and int(score.text)<=1000:
        print("the score in the good range")
        return True
    else:
        print("the score out of the range")
        return False





'''
This function is call our tests function
The main function will return -1 as an OS exit code if the tests failed and 0 if it passed."
'''
def main_function():
    print("Hello, please enter application URL (for example http://192.168.99.102:5000/)")
    # application_URL = 'http://192.168.99.102:5000/' #input()
    print("Reading the URL address from config file located at \\Tests\\application_URL.txt")

    try:
        url_address_file = open("application_URL.txt", "r")
        application_URL = url_address_file.read()
        url_address_file.close()

    except IOError:
        print("error IOFile, check if the file is located at \\Tests\\application_URL.txt")


    application_URL = application_URL+":"+PORT_NUM+"/"

    if(scores_test_service(application_URL)==True):
        print("PASS")
        return 0
    else:
        print("Fail")
        return -1

main_function()





