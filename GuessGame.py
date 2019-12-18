import random

def generate_number(difficulty):
    #generate number from 1 to difficulty
    return (random.randrange(1, difficulty+1, 1))

def get_guess_from_user(difficulty):
    #ask the user for a guess number and return it
    try:
         user_guess = int(input("Please guess a number between 1 to "+str(difficulty)))
    except:
        user_guess = 0
    while not (user_guess > 0 and user_guess <= difficulty):
        try:
            user_guess = int(input("Please guess a number between 1 to " + str(difficulty)))
        except:
            user_guess = 0

    return user_guess

def compare_results(difficulty, secret_number):
    #compare the generate number to the guessed user number
    diff = get_guess_from_user(difficulty)
    return (diff == secret_number)

def play(difficulty):
    #call all the functions and return the result
    generate_num = generate_number(difficulty)
    result = compare_results(difficulty, generate_num)

    return result
