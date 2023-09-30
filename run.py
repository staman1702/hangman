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
    selects one random word to return.
    """
        
    words = ["canal", "mango" , "fruit", "banana", "brain", "google"]

    # getting random word
    randomWord = random.choice(words)

    print(randomWord)


def main():
    """
    Run all program functions
    """
    get_random_word()
    
main()