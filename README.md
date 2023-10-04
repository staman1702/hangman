# HANGMAN

Hangman is a student-made app that lets you pass time and have some carefree fun playing simple game of hangman. 
It's designed for single play only and declares a winner once the player guessed all the letters in mystery word. 
The user is allowed to input one letter at time and is only permitted to input wrong letter 7 times. 
If all letters are not revealed, game ends in a loss. 


![Responsive](assets/images/am_i_responsive.webp)

## User Experience (UX)

### User stories

First Time Visitor Goals

- Introducing the player to well known classical game.
- Providing simple and self-explanatory entertainment.
- Enjoying the game of wits against randomly generated words.
- Ability to replay the game after every round.

Frequent User Goals

- Reliving the joy of the first visit.
- Getting more skilled every time the game is played.

## Features


### Word selection

- Mystery word is selected randomly from a Google Sheet or from small backup list in case of any problems with accessing Google Sheet.


### Game Interface

- Welcome message is shown on launch, followed by fully dashed mystery word.
- Displays number of allowed errors and ask player to input the first guess.
- If guess is correct the letter will be revealed in its proper position in word
- If guess is incorrect number of allowed errors will decrease by one
- If guess is more than one character, symbol or already been input by player,
game will notify the player and ask for new input

### End of round
- End of round message is displayed, along with fully revealed mystery word.
- After failing or managing to solve the word game offer a player a chance to play again.
- Decision is made by inputting "y" or "Y" to play again or any other key not to. 

## Testing

- Launching game: test PASSED, game launches, displays intro and generates word
- Dashed word: test PASSED, mystery word is displayed(masked) as dashes
- User inputs character: test PASSED, single alphabetical character inputs are recognized as a valid input
- User inputs multiple characters at once: test PASSED, string of multiple characters are recognized as not valid inputs
- User inputs symbols: test PASSED, non-alphabetical characters are recognized as not valid inputs
- Word contains guessed letter: test PASSED, letter that is input by user and is in the word is displayed in it's correct position in the word
- Word contains guessed letter in multiple positions: test PASSED, letter that is input by user and is in the word in more then one place is displayed in it's correct positions in the word
- Outcome 1: Game ends in loss: test PASSED, game ends after making too many mistakes, appropriate message displayed
- Outcome 2: Game ends in win: test PASSED, game ends after guessing all the letters, appropriate message displayed
- Replay game: test PASSED, finished round is successfully restarted after inputting both upper or lower case letter 'Y', whitespace after 'Y' is ignored by the game
- Refuse to replay game: test PASSED, after finished round, user's reply no to play again passes testing successfully

[View deployed site here](https://https://ci-hangman-matija-263cf48b7d7a.herokuapp.com/)

### Validator Testing

- Python code was Validated using the [PEP8](https://pep8ci.herokuapp.com/).

## Deployment

- Game has been deployed to Heroku.com following these steps:

1. Log into Heroku.com
2. Select "Create new app"
3. Choose name and region for the app
4. Select "Create app"
5. Go to "settings" tab
6. Click "Reveal Config Vars"
7. Add a Config Var in the Heroku settings, with the key CREDS and the value pasted from creds.json
8. Add "python" and "nodejs" buildpack (in this order)

9. Go to "deploy" tab
10. Under deployment method select "GitHub"
11. Search for repository to connect to
12. Click "Connect"
13. Go to "Manual deploy", select "main branch" and click "Deploy Branch"

## Credits

- Content was created and assessed by Matija Stankovic

###

- Completion of an app and it's features would not have been possible without the support and advice of my mentor Brian Macharia