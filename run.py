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


def get_random_word():
    """
    Collects all the words in our sheet and 
    selects one random word to return. Uses try/except
    to avoid network or API complications without
    breaking the game.  
    Returns:
        string: word that is goal of the game
    """   
    try:
        words_sheet = SHEET.worksheet("words")

        # all words are in first column of google sheet
        words = words_sheet.col_values(1)  

        # getting random word
        word = random.choice(words)
    except:

        #backup words if there is any problem accessing Google spreadsheet 
        backup_words = ["backup", "alternate" , "substitute", "auxiliary", "spare", "backing"]

        #randomly select backup word
        word = random.choice(backup_words)
    
    return word


def play_round(guesses, errors, game_over):
    """
    Receives 0 guesses, 7 errors and false game_over, calls function ot generate random word,
    plays the round until the complete word is guessed or allowed errors go down to 0
    Args:        
        guesses: list: all the characters that player has input in attempt to solve win the game
        errors: int: number of errors player made
        game_over: bool: while False, game continues, ends game when True
    Returns:
        string: either victorious or loss
    """
    
    game_intro_text()
    word = get_random_word()
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

    dashed_word(word, guesses)
    game_over_text()
    if game_over:
        print(f"You Won! The word was {word.upper()}.")
    else:
        print(f"You lost! The word was {word.upper()}.")


def validate_data(value, guesses):
    """    
    Validates the input data (guesses)
    Args:
        value: any type of input: player provided data
        guesses: list: all the characters that player has input prior to inputting 'value'
    Returns:
        string: if value of input does not satisfy conditions set by game
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
    """
    Take variable 'word' and 'guesses' list to 
    displays word using dashes and reveals any guessed letter that 
    player inputs. 

    Args:
        word: string: goal of the game
        guesses: list: all the characters that player inputs in his try to reveal the word
    Returns:
        string: fully or partially dashed guessed word
    """
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")            
        else:
            print("_", end=" ")            
    print("")
    print(" ")


def game_intro_text():
    """
    No Args.
    Returns: strings
    """  
    print("\n******************************")
    print("***Welcome to Hangman game.***")
    print("******************************")
    print("\n")


def game_over_text():  
    """
    No Args.
    Returns: strings
    """  
    print("\n******************************")
    print("**********Game Over.**********")
    print("******************************")
    print("\n")


def initialize_game():

    """
    Initializes game, and after complition of 
    the round, offers player to play again or
    stop
    """
    keep_playing = True

    while keep_playing:
        errors = 7
        game_over = False
        guesses = []

        play_round(guesses, errors, game_over)

        keep_playing_response = input(
            "\nWould you like to play again? "
            "Y for yes, anything else for No. "
        ).strip().lower()

        keep_playing = (keep_playing_response == 'y')

    print("\nThank you for playing, good bye!")

def main():
    """
    Run all program functions
    """       
    initialize_game()
    

main()