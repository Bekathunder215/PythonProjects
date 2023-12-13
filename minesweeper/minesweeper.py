import random
import re

class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

    #create boiard
        self.board = self.makenewboard()
        self.assignvaluestoboard()
    #initialize a set to lkeep track of locations uncovered
        self.dug = set()

    def makenewboard(self):
        board = [[None for _ in range(self.dim_size)]for _ in range(self.dim_size)] 
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 -1)
            row = loc // self.dim_size #how many times dim_size goes into loc to tell us the index of row
            col = loc % self.dim_size #what remains after dim_size with loc to tell us the index of col
            if board[row][col] == '*':
                #this means we have planted already and we keep going
                continue

            board[row][col] = '*' 
            bombs_planted += 1
        return board

    def assignvaluestoboard(self):
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                continue #if lready a bomb
            self.board[r][c] = self.getnumneighboringbomb(r, c)

    def getnumneighboringbomb(self, row, col):
        #we iterate through each of the neighboring positions and sum the number of bombs
        #top left (row-1 col-1)
        #top middle (row-1, col)
        #top right (row-1, col+1)
        #right (row, col +1)
        #left (row, col-1)
        #bottom left (row-1, col-1)
        #bottom middle (row-1, col)
        #bottom right (row-1, col+1)
        numneighboringbombs = 0
        for r in range(max(0, row-1), min(self.dim_size-1, (row+1)+1)):
            for c in range(max(0, col-1), min(self.dim_size-1, (col+1)+1)):
                if r == row and c == col:
                    continue
                if self.board[r][c] == '*':
                    numneighboringbombs += 1
        return numneighboringbombs

    def dig(self, row, col):
        self.dug.add((row, col))
        if self.board[row][col] == '*':
            return False
        else:
            return True
        for r in range(max(0, row-1), min(self.dim_size-1, (row+1)+1)):
            for c in range(max(0, col-1), min(self.dim_size-1, (col+1)+1)):
                if (r, c) in self.dug:
                    continue
                self.dif(r, c)
        
        return True

    def __str__(self):
        visible = [[None for _ in range(self.dim_size)]for _ in range(self.dim_size)] 
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row, col) in self.dug:
                    visible[row][col] = str(self.board[row][col])
                else:
                    visible[row][col] = ' '
        #put this in a string
        string_rep = ''
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible)
            widths.append(len(max(columns, key = len)))

        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'

        for i in range(len(visible)):
            row = visible[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += '  |'.join(cells)
            string_rep += '  |\n'
        
        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep


def play(dim_size = 10, num_bombs=10):
    #step 1 create the board and plant   
    board = Board(dim_size, num_bombs)
    #step 2 show the board and ask where to dig

    #step 3 if bombg show game over  if not dig recursively until each square is next to bomb
    #step 4 repeat 2 and 3
    safe = True
    while len(board.dug) < board.dim_size **2  - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*', input("Where would you liek to dig? Input as row, col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print("Invalid location. Try again.")
            continue
        safe = board.dig(row, col)
        if not safe:
            break

    if safe:
        print("Congrats! You ave won! You are really good with handling bombs")
    else:
        print("BOOOOMMMM!!!!, bye bye")
        board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]

if __name__ == '__main__':
    play()