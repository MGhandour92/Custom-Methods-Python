#Imports
from random import randint

# Variables - Constants
#---------------------------
Actual = randint(1,100) 
Guess = '' 
guesses = 0
print('act = '+ str(Actual))
#---------------------------

while(Guess != Actual):
    Guess = int(input("Guess the number")) 
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
   