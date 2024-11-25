# wordle

The game of Wordle is simple to play. In each game a 5 letter English word is chosen.
The player gets six attempts to guess this five letter word. Each guess is limited to be a
real word (I.E. the game only accepts real words as guesses, typing not-a-word will not cost
a guess) After each guess the player is given a clue as feedback. This clue will present the
players last guess with colors annotating each letter
1. Green – a letter is green to indicate the secret word has the same letter in this position
as the guess
2. Yellow – a letter is yellow to indicate that the secret word contains this letter, but not
at this position
3. Grey – a letter is typically grey to indicate that the word does not contain this letter.

wordle.py script is a normal Wordle game. easy_world.py is ”Easy mode." It tells you how many possible words are left, and provide you with a sample of possible words after each guess

#### Installation

Clone the repo

`https://github.com/umutulay/wordle.git`

## Usage

`python wordle.py`

`python easy_wordle.py`

## Authors

* Umut Tulay
