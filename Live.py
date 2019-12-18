import MemoryGame, GuessGame
from Utils import ERROR_MESSAGE
from Score import  add_score

def welcome(name):
    print("Hello "+name+" and welcome to the World of Games (WoG).\nHere you can find many cool games to play.")

def load_game():
    #ask the user to choose a game
    try:
        input_game = ("Please choose a game to play:\n"
                          "1. Memory Game - a sequence of numbers will appear for 1 second and you have to guess it back\n"
                          "2. Guess Game - guess a number and see if you chose like the computer")
        game_chosen = int(input(input_game))
    except:
        game_chosen = 0

    while (game_chosen != 1 and game_chosen != 2):
        print(ERROR_MESSAGE)
        try:
            game_chosen = int(input(input_game))
        except:
            game_chosen = 0
    #ask the user to choose the difficulty
    try:
        input_difficulty = "Please choose game difficulty from 1 to 5:"
        difficulty_chosen = int(input(input_difficulty))
    except:
        difficulty_chosen = 0

    difficulty_list = [1,2,3,4,5]

    while (difficulty_chosen not in difficulty_list):
        try:
            print(ERROR_MESSAGE)
            difficulty_chosen = int(input("Please choose game difficulty from 1 to 5:"))
        except:
            difficulty_chosen = 0
    #play the MemoryGame
    if(game_chosen == 1):
        game_result = MemoryGame.play(difficulty_chosen)
        if (game_result == True):
            add_score(difficulty_chosen)
            print("Well done, your score in this game is: " + str(difficulty_chosen))
        else:
            print("Let's try again")
            load_game()
    #play the GuessGame
    elif(game_chosen == 2):
        game_result = GuessGame.play(difficulty_chosen)
        if (game_result == True):
            add_score(difficulty_chosen)
            print("Well done, your score is: " + str(difficulty_chosen))
        else:
            print("Let's try again")
            load_game()



