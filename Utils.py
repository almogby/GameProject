import os
import time

global ERROR_MESSAGE
global SCORES_FILE_NAME

ERROR_MESSAGE = "Something went wrong.."
SCORES_FILE_NAME = "Scores.txt"

#cleen the screen after 0.7 seconds
def screen_cleaner():
    time.sleep(0.7)
    os.system('cls' if os.name == 'nt' else 'clear')
