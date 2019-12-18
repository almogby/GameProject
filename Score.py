from Utils import SCORES_FILE_NAME

def add_score(points):
    #update the current score of the user in an existing scores file
    try:
        scores_file = open(SCORES_FILE_NAME,'r+')
        current_score = scores_file.read()
        updated_score = int(current_score) + int(points)
        scores_file.seek(0)
        scores_file.write(str(updated_score))
        print("Your new total score is: " + str(updated_score))

    #create the new score of the user in a new scores file
    except:
        scores_file = open(SCORES_FILE_NAME,'w')
        scores_file.write(str(points))
        print("Your score is: " + str(points))

    scores_file.close()




