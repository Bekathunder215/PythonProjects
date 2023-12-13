from player import RandomPlayer, GeniousComputerPlayer
import time

class TTT:
    def __init__(self, board):
        self.board = [' ' for _ in range(9)]
        self.currentwinner = None

    def printb(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')


    @staticmethod
    def printbnums():
        numberboard = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in numberboard:
            print('| ' + ' | '.join(row) + ' |')

    def availablemoves(self):
        return [i for i, spot in enumerate(self.board) if spot == ' ']
    
    def emptysquares(self):
        return ' ' in self.board

    def numemptysquares(self):
        return self.board.count(' ')
    
    def makemove(self, square, letter):
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square, letter):
                self.currentwinner = letter
            return True
        else:
            return False
        
    def winner(self, square, letter):
        row_index = square // 3
        row = self.board[row_index*3 : (row_index +1)*3]
        if all([spot == letter for spot in row]):
            return True
        col_index = square % 3
        column = [self.board[col_index+i*3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True
        if square % 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all([spot == letter for spot in diagonal2]):
                return True
        
        return False
#        moves = []
 #       for (i,spot) in enumerate(self.board):
  #          if spot == ' ':
   #             moves.append(i)
    #    return moves

def play(game, xplayer, oplayer, print_game = True):
    if print_game:
        game.printbnums()
    
    letter = 'X'
    while game.emptysquares():
        if letter == 'O':
            square = oplayer.getmove(game)
        else:
            square = xplayer.getmove(game)

        if game.makemove(square, letter):
            if print_game:
                print(letter + f" makes a move to square {square}")
                game.printb()
                print(' ')

            if game.currentwinner:
                if print_game:
                    print(letter + ' wins!')
                return letter


            letter = 'O' if letter == 'X' else 'X'
    if print_game:
        print("it's a tie!")
    time.sleep(1)


if __name__== '__main__':
    xplayer = RandomPlayer('X')
    oplayer = GeniousComputerPlayer('O')
    t = TTT(' ')
    play(t, xplayer, oplayer, print_game=True)