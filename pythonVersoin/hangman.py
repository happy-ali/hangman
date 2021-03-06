# 6.00 Problem Set 3
# 
# Hangman game
#

# -----------------------------------
# Helper code
# You don't need to understand this helper code,
# but you will have to know how to use the functions
# (so be sure to read the docstrings!)

import random
import string

WORDLIST_FILENAME = "\words.txt"#give it the location of the word list

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    i=0
    for s in lettersGuessed :
        if s in secretWord :
            i+=1
    return i == len(secretWord)



def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    wstr = ''
    for s in secretWord :
        if s in lettersGuessed :
            wstr+=s
        else :
            wstr+='_'
        wstr+=' '
    return wstr



def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # FILL IN YOUR CODE HERE...
    a=''
    abc ='abcdefghijklmnopqrstuvwxyz'
    for i in abc :
        if i in lettersGuessed :
            None
        else :
            a+=i
    return a

def hangman(secretWord):
    lettersGuessed=[]
    guess = 8
    print "Welcome to the game, Hangman!"
    print 'I am thinking of a word that is '+str(len(secretWord)),
    print ' letters long.'
    while guess > 0 :
        print '-------------'
        print 'You have '+str(guess)+' guesses left.'
        print 'Available letters: '+getAvailableLetters(lettersGuessed)
        guessLettre = raw_input('Please guess a letter: ').lower()
        if guessLettre in lettersGuessed:
            print'Oops! You\'ve already guessed that letter:',
            print getGuessedWord(secretWord, lettersGuessed)
            guess+=1
        elif guessLettre in secretWord :
            lettersGuessed += guessLettre
            guess+=1
            print 'Good guess: ',
            print getGuessedWord(secretWord, lettersGuessed) 
            if isWordGuessed(secretWord, lettersGuessed):
                break
        else :
            lettersGuessed += guessLettre 
            print 'Oops! That letter is not in my word:',
            print getGuessedWord(secretWord, lettersGuessed)
        guess-=1
    print '-------------'
    if isWordGuessed(secretWord, lettersGuessed):
        print 'Congratulations, you won!'
    else :
        print 'Sorry, you ran out of guesses. The word was '+secretWord+'.'
secretWord = chooseWord(wordlist)
hangman(secretWord)

# When you've completed your hangman function, uncomment these two lines
# and run this file to test! (hint: you might want to pick your own
# secretWord while you're testing)

# secretWord = chooseWord(wordlist).lower()
# hangman(secretWord)
