# https://youtu.be/LBKKMVUBbc4 <- tutorial video

import random

# Method to generate a secret number
def generate_secret_number():
    return random.randint(1, 50) 


# Method to evaluate the user's guess
def evaluate_guess(secret, guess):
    if guess < secret:
        return "tow low"
    elif guess > secret:
        return "too high"
    else:
        return "correct"
    

# Main function to run the game
def play_game():
    print("Welcome to the Number Guessing Game!")
    print("I have selected a secret number between 1 and 50. Can you guess it?")
    print("You only have 5 attempts!!")
    
    secret_number = generate_secret_number()
    print(secret_number) # for testing purposes, you can comment this out in the final version
    secret_number = generate_secret_number()
    print(secret_number) # for testing purposes, you can comment this out in the final version
    attempts = 0
    max_guesses = 5
    print
    while attempts < max_guesses:
        guess = input(f"Attempt {attempts + 1}: Enter your guess: ")
        
        # input validation
        try:
            guess = int(guess)
        
        except:
            print("Not a valid input. Input must be an integer between 1 and 50.")
            continue
        
        attempts += 1
        
        result = evaluate_guess(secret_number, guess)
        
        if result == "correct":
            print(f"Correct number. Your guess of {guess} is correct! You won the game in {attempts} attempts!")
            return
        else:
            print(f"Your guess is {result}.\n")
            
    print(f"Your ran out of guesses. The secret number was {secret_number}. Better luck next time!")
    
play_game()