#!/usr/bin/env python

"""CPU GUESS"""

from random import randint

def main():
    randomNumber = randint(0,100)
    cpuGuess = randint (0,100)
    timeGuessed = 0
    timeGuessedHigh = 0
    timeGuessedLow = 0
    ans = 0
    while ans == 0:
        if (cpuGuess == randomNumber):
            print ("The computer guessed:")
            print (timeGuessed)
            print ("the computer has guessed too high:")
            print (timeGuessedHigh)
            print ("the computer has guessed too low:")
            print (timeGuessedLow)
            print ("the number guessed was:")
            print (randomNumber)
            ans = 1
        else:
            cpuGuess = randint (0,100)
            timeGuessed +=1
            if (cpuGuess > randomNumber):
                timeGuessedHigh +=1
            else:
                timeGuessedLow +=1
main()





    
