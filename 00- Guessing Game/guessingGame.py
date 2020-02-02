'''
Guessing Game:
    A program that picks a random integer from 1 to 100, and has players guess the number. The rules are:
    If a player's guess is less than 1 or greater than 100, say "OUT OF BOUNDS"
    On all turns, if a guess is
    closer to the number than the previous guess return "Closer!"
    farther from the number than the previous guess, return "Farther!"
    When the player's guess equals the number, tell them they've guessed correctly and how many guesses it took!
    Now Lets o fro the Steps!
'''

#Imports
from random import randint

def myGuessingGame():    
    # Variables - Constants
    #---------------------------
    Actual = randint(1,100) 
    Guess = '' 
    guesses = 0
    print('act = '+ str(Actual))
    #---------------------------

    #as long as the user didn't reach the number, continue looping
    while(Guess != Actual):
        #take user input
        Guess = int(input("Guess the number: ")) 
        #if user guessed correctly, then break
        if Guess == Actual:
            print ("Wow, you've guessed Correctly this time") 
            print ('You have guessed it in {} times\n'.format(guesses))
            break

        elif Guess >= 1 and Guess <= 100:
            if abs(Actual - Guess) <= 10:
                print ("You are Close, Enter next guess\n")
            elif abs(Actual - Guess) >= 10:
                print ("You are Far, Enter next guess\n")

        else:
            print('OUT OF BOUNDS, Enter next guess\n')
            
        guesses +=1


#==================================================================