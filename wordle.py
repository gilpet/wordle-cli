import random
import os
import json

green = '\033[92m'
yellow = '\033[93m'
red = '\033[91m'
default_colour = '\033[0m'

five_letter_dictionary = {}

with open('5letterdict.json', 'r') as f:
    five_letter_dictionary = json.load(f)

possible_words = five_letter_dictionary.keys()
alphabet = {'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'}
word_of_the_day = random.choice(possible_words)
colour_to_character_dict_list = [{'': ''}, {'': ''}, {'':''}, {'':''}, {'':''}]
characters_not_in_word = []
guesses_left = 6
attempts = []

def clear_screen():
    os.system('cls' if os.name=='nt' else 'clear')

def find(character):
    return [i for i, letter in enumerate(word_of_the_day) if letter == character]

def print_results():
    print_result = []
    for colour_to_letter in colour_to_character_dict_list:
        for colour in colour_to_letter:
            print_result.append(colour + colour_to_letter[colour].capitalize())
    clear_screen()
    print(default_colour + '\nThese are not in the word: ' + red + ' '.join([str(char).capitalize() for char in sorted(set(characters_not_in_word))]))
    print(default_colour + '\nRemaining Letters: ' + ' '.join([str(char).capitalize() for char in sorted(alphabet.difference(set(characters_not_in_word)))]))
    return ' '.join([str(colour_letter) for colour_letter in print_result])

def check_word(word):
    char_index = 0
    for character in word:
        result = find(character)
        if len(result) == 0:
            colour_to_character_dict_list[char_index] = {default_colour : character}
            characters_not_in_word.append(character)
        elif char_index in result:
            colour_to_character_dict_list[char_index] = {green : character}
        else:
            colour_to_character_dict_list[char_index] = {yellow : character}
        char_index += 1
    return print_results()

while (guesses_left > 0):
    guesses_left -= 1
    invalid_guess = True
    guess = ''
    while invalid_guess:
        guess = raw_input(default_colour + '\nEnter a 5 letter word: \n\n')
        invalid_guess = len(guess) is not 5 or guess not in possible_words
    if guess == word_of_the_day:
        print('\nYOU WIN!!!!!!!!!!!!!!!!!!!!!!!\n')
        print(five_letter_dictionary[word_of_the_day])
        exit()
    attempt = check_word(guess)
    print('\nGuesses Remaining: ' + str(guesses_left) + '\n')
    attempts.append(attempt)
    for attempt in attempts:
        print(attempt)
print('\nyou lose bud :(')
print('The word was: ' + word_of_the_day)
print('\n' + five_letter_dictionary[word_of_the_day])
