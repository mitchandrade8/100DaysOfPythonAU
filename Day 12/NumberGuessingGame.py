
from random import randint
# Guess the number game

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

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
def set_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if level == "easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

# Let the user guess a number
guess = int(input("Make a guess: "))
turns = set_difficulty
print(f"You have {turns} attempts remaining to guess the number.")
# Track the number of turns and reduce by 1 if they get it wrong

# Repeat the guessing functionality if they get it wrong
