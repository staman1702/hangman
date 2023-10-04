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

### Validator Testing

## Deployment

## Credits