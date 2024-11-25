# Umut Tulay
# Wordle Game
from display_utility import green, grey, yellow
from words import words
import random


def check_word(secret, guess):
    """
    This function checks the letter in the words if they are in correct order with secret. If the letter is in correct
    order, it is green. If the letter is in secret but in a different order in guess, it is yellow. If the letter is not
    in secret, it is grey.

    Parameters:
    secret: secret word for Wordle game
    guess: input word input by the user

    Return:
    final list: list containing colors
    """
    comparison_list = []
    secret_double_letters = {}
    guess_double_letters = {}

    for char in range(len(guess)):  # check if it is green, yellow or grey without thinking double letters
        if guess[char] == secret[char]:
            comparison_list.append((guess[char], 'green'))
        else:
            found = False
            for search in secret:
                if search == guess[char]:
                    comparison_list.append((guess[char], 'yellow'))
                    found = True
                    break
            if not found:
                comparison_list.append((guess[char], 'grey'))

    def double_letter_func(word, dictio):  # check if there are any double letters in a word
        for letter in word:
            if letter in dictio:
                dictio[letter] += 1
            else:
                dictio[letter] = 1
        return dictio

    double_letter_func(secret, secret_double_letters)
    double_letter_func(guess, guess_double_letters)

    count = 0
    for key, value in guess_double_letters.items():
        if value >= 2 and secret_double_letters.get(key) is not None and guess_double_letters[key] > \
                secret_double_letters[key]:
            for item in comparison_list:
                if item == (key, "green"):  # green has priority over yellow
                    count += 1
                    if count == secret_double_letters[key]:  # if green is equal to double letters, make the rest gray
                        for i in range(len(comparison_list)):
                            if comparison_list[i] == (key, "yellow"):
                                comparison_list[i] = (key, "grey")
                                value -= 1
                elif value >= 2:  # we have more yellow than necessary
                    number_loop = guess_double_letters[key] - secret_double_letters[key]
                    count_again = 0
                    for j in range(len(comparison_list) - 1, -1, -1):
                        # starting from the end, make grey until number of double letters are same
                        if comparison_list[j] == (key, "yellow"):
                            comparison_list[j] = (key, "grey")
                            count_again += 1
                        if count_again == number_loop:
                            value -= 1
                            break

    final_list = []
    for item in comparison_list:
        final_list.append(item[1])
    return final_list


def known_word(clues):
    """
    This function is to help with “basic recordkeeping” for the end-user of our code
    Positions which have not seen a green clue are presented as _ and positions which have received
    a green clue are the known letter.

    Parameters:
    clues: a list containing a record of guesses taken and clues received so-far.

    Return:
    my_string: string indicating what we know about the secret word according to green hints seen so-far.
    """
    record_guess = ['_', '_', '_', '_', '_']

    if clues:
        for items in clues:
            guess, colors = items[0], items[1]
            for i, color in enumerate(colors):
                if color == "green":
                    record_guess[i] = guess[i]
                elif record_guess[i].isalpha():
                    pass
                else:
                    record_guess[i] = '_'

    record_guess = ''.join(record_guess)
    return record_guess


def no_letters(clues):
    """
    This function will be the grey letters that are not in a secret word

    Parameters:
    clues: a list containing a record of guesses taken and clues received so-far.

    Return:
    sorted_non_used_letters: string indicating the grey letters in a sorted order
    """
    used_letters = set()
    not_used_letters = set()

    if clues:
        for items in clues:
            guess, colors = items[0], items[1]
            for i, color in enumerate(colors):
                if color == "green" or color == "yellow":
                    used_letters.add(guess[i])
                elif color == "grey":
                    for j in range(i + 1, len(colors)):
                        if guess[i] == guess[j] and (colors[j] == "green" or colors[j] == "yellow"):
                            used_letters.add(guess[i])
                    if guess[i] not in used_letters:
                        not_used_letters.add(guess[i])

    sorted_non_used_letters = sorted(not_used_letters)
    return ''.join(sorted_non_used_letters)


def yes_letters(clues):
    """
    This function will be the yellow and green letters that are in a secret word

    Parameters:
    clues: a list containing a record of guesses taken and clues received so-far.

    Return:
    sorted_used_letters: string indicating the yellow and green letters in a sorted order
    """
    used_letters = set()
    not_used_letters = set()

    if clues:
        for items in clues:
            guess, colors = items[0], items[1]
            for i, color in enumerate(colors):
                if color == "green" or color == "yellow":
                    used_letters.add(guess[i])
                elif color == "grey":
                    for j in range(i + 1, len(colors)):
                        if guess[i] == guess[j] and (colors[j] == "green" or colors[j] == "yellow"):
                            used_letters.add(guess[i])
                    if guess[i] not in used_letters:
                        not_used_letters.add(guess[i])

    sorted_used_letters = sorted(used_letters)
    return ''.join(sorted_used_letters)


def game(secret):
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
        print("Known: " + known_word(clues_list))
        print("Green/Yellow Letters: " + yes_letters(clues_list))
        print("Grey Letters: " + no_letters(clues_list))
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
        if secret_lower == guess_word:
            break
    print("Answer: " + secret)


if __name__ == "__main__":
    """Main function to start a game and choose random secret word"""
    random_word = random.choice(words)
    game(random_word)
