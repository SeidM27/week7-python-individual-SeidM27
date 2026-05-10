# Project 2 — Number Guessing Game
# Author: your name here

import random

# TODO: generate a random secret number between 1 and 10

# TODO: set up a guesses counter

# TODO: get the user's first guess

# TODO: while loop — keep asking until the guess is correct
#   - print "Too low!" or "Too high!" on each wrong guess
#   - count each guess

# TODO: print the congratulations message with the number of guesses
# Project 2 - Number Guessing Game
# Author: Seid Mamuti
import random
# Pick a random number between 1 and 10
secret = random.randint(1, 10)
# Counter for number of guesses
guesses = 0
# Ask the user for the first guess
guess = int(input("Guess a number between 1 and 10: "))
guesses += 1
# Repeat while the guess is not correct
while guess != secret:
if guess < secret:
guess = int(input("Too low! Try again: "))
else:
guess = int(input("Too high! Try again: "))
guesses += 1
print(f"Correct! You got it in {guesses} guesses.")
