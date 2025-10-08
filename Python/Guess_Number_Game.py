#!/bin/env python3

# Task 4: Guess the Number Game
# The program randomly selects a number and gives hints

import random
import sys  # Needed to exit the program

print("=== Guess the Number Game ===")
secret_number = random.randint(1, 50)

while True:
    guess = int(input("Guess a number between 1 and 50: "))

    # Check if input is outside the valid range
    if guess < 1 or guess > 50:
        print("❌ Invalid input! Please enter a number between 1 and 50. Exiting game...")
        sys.exit()  # Immediately exits the program
    
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("🎉 Correct! You guessed the number!")
        break
