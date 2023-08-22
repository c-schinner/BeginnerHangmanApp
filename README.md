# Hangman Game
Welcome to the Beginner Hangman Game! Test your word-guessing skills and try to uncover the hidden word before running out of lives. With each guess, you'll get closer to solving the puzzle or face the consequences of guessing incorrectly.

# How to Play
Run the program using a Python interpreter (Python 3 recommended).
The game will randomly select a word from the provided list of words.
You will be shown a hint indicating the length of the chosen word.
A series of underscores will represent the letters in the chosen word.
Guess a letter and see if it matches any positions in the word.
The game will reveal the positions of the correctly guessed letters.
Keep guessing letters until you either solve the puzzle or run out of lives.

# Winning and Losing
If you correctly guess all the letters in the chosen word before running out of lives, you win!
If you run out of lives, the game ends, and you lose.

# Example Gameplay
HINT... the chosen word is camel
['_', '_', '_', '_', '_']

Pick a letter: c
['c', '_', '_', '_', '_']

Lives Remaining = 6
Letters not in the word

Pick a letter: a
['c', 'a', '_', '_', '_']

Lives Remaining = 6
Letters not in the word

Pick a letter: e
['c', 'a', '_', 'e', '_']

You've already guessed e, try another letter.
Lives Remaining = 6
Letters not in the word

...

Congratulations you've WON!
Thanks for playing!

# Tips
Pay attention to the hint provided at the beginning of the game.
Keep track of the letters you've guessed and the ones that are not part of the word.
Try to solve the puzzle before running out of lives.

# How to Run
Save the code to a .py file (e.g., hangman_game.py).
Open a terminal or command prompt.
Navigate to the directory where the file is located.
Run the program by entering python hangman_game.py.

Enjoy the challenge of the Beginner Hangman Game and see if you can guess the hidden words!
