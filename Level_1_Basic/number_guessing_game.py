# Task 2: Number Guessing Game

# Description: Write a program that randomly generates
# a number between 1 and 100. The user has to guess
# the number, and the program will give feedback if the
# guess is too high or too low.

# Objectives:
# a. Use the random module to generate a random number.
# b. Give the user multiple attempts to guess the number.
# c. Provide appropriate feedback (e.g., "Too high" or "Too low").
# d. Exit the game if the user guesses correctly or after a
# maximum number of attempts.

import random


def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number within the range of 1 to 100.")
                continue

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if attempts == max_attempts and guess != secret_number:
        print(f"Sorry, you've used all your attempts. The number was {secret_number}.")


if __name__ == "__main__":
    number_guessing_game()
# Task 2: Number Guessing Game

# Description: Write a program that randomly generates
# a number between 1 and 100. The user has to guess
# the number, and the program will give feedback if the
# guess is too high or too low.

# Objectives:
# a. Use the random module to generate a random number.
# b. Give the user multiple attempts to guess the number.
# c. Provide appropriate feedback (e.g., "Too high" or "Too low").
# d. Exit the game if the user guesses correctly or after a
# maximum number of attempts.

import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    max_attempts = 10
    attempts = 0

    print("Welcome to the Number Guessing Game!")
    print("I have selected a number between 1 and 100.")
    print(f"You have {max_attempts} attempts to guess it.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1

            if guess < 1 or guess > 100:
                print("Please guess a number within the range of 1 to 100.")
                continue

            if guess < secret_number:
                print("Too low!")
            elif guess > secret_number:
                print("Too high!")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} in {attempts} attempts.")
                break
        except ValueError:
            print("Invalid input. Please enter a valid number.")

    if attempts == max_attempts and guess != secret_number:
        print(f"Sorry, you've used all your attempts. The number was {secret_number}.")


if __name__ == "__main__":
    number_guessing_game()