# Umut Tulay
# Easy Wordle Game
from display_utility import green, grey, yellow
from words import words
from wordle import check_word
import random


def filter_word_list(words, clues):
    """
    This function is to find possible secret words according to the given clue

    Parameters:
    words: long word list
    clues: a list containing a record of guesses taken and clues received so far.

    Return:
    full_word_list, words, final_list: a new word list containing only the words in the input word list
    which could be the secret word
    """
    final_list = []
    full_word_list = words.copy()

    if len(clues) == 0 or len(clues) == 1:
        if len(clues) == 0:
            return words
        for new_word in words:
            upper_new_word = new_word.upper()
            guess, colors = clues[0][0], clues[0][1]
            new_word_colors = check_word(upper_new_word, guess)
            if new_word_colors == colors:
                final_list.append(new_word)
            else:
                pass
        return final_list

    elif len(clues) > 1:  # if more than one clues, we need to make a new list according to the new clue
        for item in clues:
            guess, colors = item[0], item[1]
            temp_list = []
            for old_words in full_word_list:
                upper_old_words = old_words.upper()
                new_word_colors = check_word(upper_old_words, guess)
                if new_word_colors == colors:
                    temp_list.append(old_words)
            full_word_list = temp_list
    return full_word_list


def easy_game(secret):
    """
    This function is a playable wordle game. It mostly prints the game, including the previous functions.

    Parameters:
    secret: secret word for Wordle game

    Return:
    no return
    """
    secret_lower = secret.lower()
    clues_list = []
    guess_limit = 6

    for i in range(guess_limit):
        print("> ", end="")
        guess_word = input()
        while guess_word not in words or len(guess_word) > 5:
            print("Not a word. Try again")
            print("> ", end="")
            guess_word = input()
        color_list = check_word(secret_lower, guess_word)
        upper_guess = guess_word.upper()
        clue = (upper_guess, color_list)
        clues_list.append(clue)
        for items in clues_list:
            word, colors = items[0], items[1]
            for j in (range(len(colors))):
                if colors[j] == "grey":
                    grey(word[j])
                elif colors[j] == "green":
                    green(word[j])
                elif colors[j] == "yellow":
                    yellow(word[j])
            print()

        possible_list = filter_word_list(words, clues_list)
        print(len(possible_list), "words possible:")
        random.shuffle(possible_list)
        if len(possible_list) > 5:
            for number in range(5):
                print(possible_list[number])
        else:
            for number in range(len(possible_list)):
                print(possible_list[number])
        if secret_lower == guess_word:
            break
    print("Answer: " + secret)


if __name__ == "__main__":
    """Main function to start a game and choose random secret word"""
    random_word = random.choice(words)
    easy_game(random_word)
