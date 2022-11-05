#!/usr/bin/python3
import re
import random
import json
from urllib import request

# ==================== FUNCTION =====================================

# function to remove spaces from a string
def remove(string):
    return "".join(string.split())

# ================== REST API - GET REQUEST =========================

# api GET request to ipwhois at ip addr 8.8.4.4
ip = '8.8.4.4'
response = request.urlopen('http://ipwho.is/' + ip)
ipwhois = json.load(response)

# store the value of 'country' from the json object 'ipwhois'
country = ('{0}'.format(ipwhois['country'])).lower()

# ===================== HANGMAN GAME ==============================

# create a list of words to be used for the game
words = ['coffee', 'banana', 'airport', 'cryptography', 'computer']
words.append(remove(country)) # invoke function to remove any spaces

# choose a random word from the array
chosenWord = random.choice(words)

# number of lives the player has before losing
lives = 5

# array that stores all the letters that a player submits
letters = []

# prompt user with start of game
print('------------- Welcome to Hangman -------------')
print('Thank you for playing Hangman! Give me a moment to select the hidden word...\n')
print('The word has been selected... ready to play!\n')

# as long as a player has remaining lives, the loop continues
while lives != 0:

    # count remaining letters to guess
    charactersLeft = 0

    # loop through all characters of the word
    for character in chosenWord:

        # make the letter a string
        letter = str(character)

        # if the letter in the loop is in our array of used letters, we write
        # the letter, otherwise we show an underscore (as a letter left to guess)
        if letters.__contains__(letter):
            print(letter, end=" ")
        else:
            print('_', end=" ")

            # decrease the count of letters left, used to track whether the
            # game is finished or not
            charactersLeft += 1

    print("\n") # new line break
    
    #print out letters for the user to reference
    print('list of letters you have chosen: ')
    for i in letters:
        print(i, end=" ")
    
    print("\n") # new line break

    # if there are no characters left, the game is over and we can break out of the loop
    if charactersLeft == 0:
        break
    else:
        print('Characters remaining: ' + str(charactersLeft) + '\n')

    key = input('Please enter a letter: ')

    print("\n") # new line break

    # using the regex above, we check if the submitted character is valid
    if not re.match('[a-z]', key):
        print('The letter ' + key + ' is invalid. Try again!\n')
        continue

    # check if the letter is already in our array
    # else, add it to the array
    if letters.__contains__(key):
        print('You already entered this letter!\n')
    else:
        letters.append(key)

    print('========================================\n')

    # if the chosen word doesn't contain the given letter, we reduce the number
    # of lives left by one
    if not (chosenWord.__contains__(key)):
        lives -= 1

        # if all the lives ran out, show message below
        if lives > 0:
            print('The letter ' + str(key) + ' is not in the word. Attempts left: ' + str(lives) + '\n')

if lives > 0:
    print('============ GAME OVER =================\n')
    print('You won with ' + str(lives) + ' live(s) left!\n')
    print('========================================')
else:
    print('============ GAME OVER =================\n')
    print('You lost! The hidden word was ' + str(chosenWord) + '\n')
    print('========================================')