
# Step 2

import random

word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)

# Testing code
print(f'Pssst, the solution is {chosen_word}')

# Todo - 1: Create an empty list called ^Display^.
# For each letter in the chosen_word, add a "_" to ^display^

# So if the chosen_word was "apple", display should be ["_", "_", "_", "_", "_"] with 5 representing each letter to guess.

guess = input("Guess a letter: ").lower()

# Todo - 2: Loop through each position in the chosen_word;
# If the letter at that position matches 'guess' then reveal that letter in the display at that position.
#e.g. If the user guessed "p" and the chosen word was "apple", then the display should be ["_". "p", "p", "_", "_"].

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("Wrong")

# Todo - 3: Print 'Display' and you should see the guessed letter in the correct position and every other letter replace with "_".
# Hint - Don't worry about getting the user to guess the next letter. We'll tackle that in step 3.



# Will think about the problems and coming problems 

