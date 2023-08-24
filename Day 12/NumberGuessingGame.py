
from random import randint
# Guess the number game

# need a vaariable to track the difficulty
# varaible to for the guess
# if the guess is correct of not 
    # if else 


# Function to check user's guess against actual answer
def check_answer(guess, answer):
    if guess > answer:
        print("Too high.")
    elif guess < answer:
        print("Too low.")
    else: 
        print(f"You got it! The answer was {answer}.")
# Choosing a random number between 1 and 100

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
answer = randint(1, 100)

# Function for difficulty

# Let the user guess a number
guess = int(input("Make a guess:"))


# Track the number of turns and reduce by 1 if they get it wrong

# Repeat the guessing functionality if they get it wrong
