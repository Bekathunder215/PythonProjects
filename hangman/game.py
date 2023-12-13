import random
from wordslist import wordlist
import string

def getword(wordlist):
    word = random.choice(wordlist)
    while '-' in word or ' ' in word:
        word = random.choice(wordlist)
    
    return word.upper()

def hangman():
    word = getword(wordlist)
    wordletters = set(word)
    alphabet = set(string.ascii_uppercase)
    usedletters = set()
    lives = 6
    
    while len(wordletters) > 0 and lives > 0:
        print("you have used: ", ' '.join(usedletters))

        wordlist1 = [letter if letter in usedletters else '_' for letter in word]
        print("Current word: ", ' '.join(wordlist1))
        userletter = input("Guess a letter: ").upper()
        if userletter in alphabet - usedletters:
            usedletters.add(userletter)
            if userletter in wordletters:
                wordletters.remove(userletter)
            else:
                lives -= 1
        
        elif userletter in usedletters:
            print("You have already used this letter. Please try again.")
        else:
            print("Invalid letter, please type a letter")
    if lives > 0:
        print("You WON!! Guess you saved the hangman!")
    else:
        print(f"You lost!! word was {word}")


hangman()