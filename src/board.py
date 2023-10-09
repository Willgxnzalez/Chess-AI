from const import *
from square import Square

class Board:
    def __init__(self):
        self.board = [[Square(r,c) for c in range(COLS)] for r in range(ROWS)]
        print(self.board)

bo = Board()
