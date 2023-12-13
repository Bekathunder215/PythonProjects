import random

def play():
    user = input("Choose: \n'r' for rock\n's' for scissors\n'p' for paper\nYour choice: ")
    computer = random.choice(['s','p','r'])

    if user == computer:
        return "It's a tie!"
    if win(user, computer):
        return "You won!!"
    
    return "You lost!"


def win(player, op):
    if (player == 'r' and op == 's') or (player == 's' and op == 'p') or (player == 'p' and op == 'r'):
        return True

print(play())