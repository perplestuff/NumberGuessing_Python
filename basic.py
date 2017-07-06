#!/usr/bin/env python

"""NUMBER GUESSER"""

from random import randint

def main():
    randomNumber = randint(0,100)
    print ("guess a number between 1 and 100.")
    ans = 0
    while ans == 0:
        userGuess = int(input("my answer: "))
        if (userGuess == randomNumber):
            print ("success")
            ans = 1
        else:
            print ("guess again")
            if (userGuess > randomNumber):
                print ("go lower.")
            else:
                print ("go higher.")

main()
