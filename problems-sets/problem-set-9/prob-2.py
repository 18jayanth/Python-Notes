""" 2. The game() function in a program lets a user play a game and returns the score
as an integer. You need to read a file ‘Hi-score.txt’ which is either blank or
contains the previous Hi-score. You need to write a program to update the Hiscore 
whenever the game() function breaks the Hi-score """
import random
def game():
    print("You are Playing a game:")
    score=random.randint(1,61)
    #Fetching data from file
    with open("highscore.txt") as f:
        high=f.read()
        if(high!=""):
            high=int(high)
        else:
            high=0
    print(f"Your Score is {score}")
    #Comparing
    if(score>high):
        with open("highscore.txt" ,"w") as f:

            f.write(str(score))
    return score
game()
    
