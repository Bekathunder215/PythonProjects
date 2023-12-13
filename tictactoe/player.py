import math
import random

class Player:
    def __init__(self, letter):
        self.letter = letter

    def getmove(self, game):
        pass

class RandomComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getmove(self, game):
        square = random.choice(game.availablemoves())
        return square

class RandomPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getmove(self, game):
        validsquare = False
        val = None
        while not validsquare:
            square = input(self.letter + "'s turn. Input move (0-8): ")
            try:
                val = int(square)
                if val not in game.availablemoves():
                    raise ValueError
                validsquare = True
            except ValueError:
                print("invalid square. Try again. ")

        return val
                

class GeniousComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def getmove(self, game):
        if len(game.availablemoves()) == 9:
            square = random.choice(game.availablemoves())
        else:
            square = self.minimax(game, self.letter)['position']
        return square
    def minimax(self, state, player):
        maxplayer = self.letter
        otherplayer = 'O' if player == 'X' else 'X'

        if state.currentwinner == otherplayer:
            return{'position' : None,
                        'score': 1*(state.numemptysquares() +1) if otherplayer == maxplayer else -1 *(state.numemptysquares() +1)
                }
        elif not state.emptysquares():
            return {'position':None, 'score':0}
            
        if player == maxplayer:
            best = {'position':None, 'score': -math.inf}
        else:
            best = {'position':None, 'score': math.inf}
            for possiblemove in state.availablemoves():
                state.makemove(possiblemove, player)
                simscore = self.minimax(state,otherplayer)
                state.board[possiblemove] = ' '
                state.currentwinner = None
                simscore['position'] = possiblemove
                if player == maxplayer:
                    if simscore['score'] > best['score']:
                        best = simscore
                else:
                    if simscore['score'] < best['score']:
                        best = simscore
        return best