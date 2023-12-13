import random

def guess(x):
    randomnum = random.randint(1,x)
    playerguess = 0
    while playerguess != randomnum:
        playerguess = input(f"Guess a number between 1 and {x}")
        if playerguess < randomnum:
            print("Sorry, guess again. Too low!!")
        elif playerguess > randomnum:
            print("Sorry, guess again. Too high!!")

    print(f"Correct!!! You win!!")

def comguess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            randomnum = random.randint(low, high)
        else:
            randomnum = low
        feedback = input(f"My guess is {randomnum}, is this too high 'h', too low 'l' or correct 'c' : ")
        if feedback == 'h':
            high = randomnum - 1
        elif feedback == 'l':
            low = randomnum + 1

    print(f"YES!! Correct!!! I win with the number {randomnum}!!")


comguess(10)

