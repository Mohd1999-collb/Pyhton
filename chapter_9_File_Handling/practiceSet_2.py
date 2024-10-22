import random

def playGame():
    n = random.randint(1, 100) # Genrate random integer  number between given range
    return str(n);


def writeScore(n) :
    with open('chapter_9_File_Handling/hiScore.txt', 'w') as f:
        f.write(n)


# n = random.random() # Genrate random floating point number between 0 and 1

with open('chapter_9_File_Handling/hiScore.txt') as f :
    hiScore = f.read()
    n = playGame()
    if hiScore == '' :
        writeScore(n)  
    else :
        if int(n) > int(hiScore) :
            writeScore(n)
        else :
            print("Your score is not high enough. Hi-score is", hiScore)