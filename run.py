import gspread
from google.oauth2.service_account import Credentials
import random

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('hangman')

errors = 7
guesses = []
game_over = False

def get_random_word():
    """
    Collects all the words in our sheet and 
    selects one random word to return.
    """   
    words_sheet = SHEET.worksheet("words")

    # all our words are in first column of our google sheet
    words = words_sheet.col_values(1)  

    # getting random word
    word = random.choice(words)
    
    return word
    

def play_game(word, guesses, errors, game_over):
    """
    Receives the word, 0 guesses, 7 errors and false game_over,
    plays the game until the complete word is guessed or allowed errors go down to 0
    """
    
    while not game_over:        
        dashed_word(word, guesses)
        guess = input(f"Errors remaining: {errors}, type your guess: ")
        if validate_data(guess, guesses):
            guesses.append(guess.lower())
            if guess.lower() not in word.lower():
                errors -= 1
                if errors == 0:
                    break

        game_over = True

        for letter in word:
            if letter.lower() not in guesses:
                game_over = False

    if game_over:
        print(f"You Won! The word was {word.upper()}.")
    else:
        print(f"You lost! The word was {word.upper()}.")


def validate_data(value, guesses):
    """    
    Raises ValueError if values are not aphabetical characters,
    have been already used in guesses or are longer than 1.
    """
    try:
        if value in guesses:
            raise ValueError(
                f"You already guessed {value}"
            )  
        elif len(value) != 1:
            raise ValueError(
                f"Exactly 1 char required, you provided {len(value)}"
            )
        elif not value.isalpha():
            raise ValueError(
                f"Please input alphabetical character! You provided {value}"
            )
    except ValueError as e:
        print(f"Invalid data: {e}, please try again.\n")
        return False

    return True


def dashed_word(word, guesses):
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
            print("_", end=" ")
    print("")


def main():
    """
    Run all program functions
    """
    get_random_word()    
    word = get_random_word()
    play_game(word, guesses, errors, game_over)
    

print("Welcome to Hangman game.")
print("************************")
main()