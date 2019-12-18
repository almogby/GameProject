import random

from Utils import screen_cleaner

#generate random list in length of difficulty
def generate_sequence(difficulty):
    generate_list = random.sample(range(1, 101), difficulty)
    print(generate_list)
    screen_cleaner()
    return generate_list

#get the guessed list from the user
def get_list_from_user(difficulty):
    print("After seeing the numbers enter the numbers you saw,\n"
          "each one separated with Enter.")
    user_list = []
    for i in range(difficulty):
        try:
            element = int(input(""))
        except:
            element = 0
        user_list.append(element)

    return user_list

#compare between the generate list and the user's guessed list
def is_list_equal(list_a, list_b):
    list_a.sort()
    list_b.sort()

    if(list_a == list_b):
        return True
    else:
        return False

#play the game
def play(difficulty):
    #get the generated list
    game_list = generate_sequence(difficulty)
    #get the user list
    user_list = get_list_from_user(difficulty)
    #check if equal
    result = is_list_equal(game_list, user_list)

    return result




