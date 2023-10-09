from const import *
from square import Square

class Board:
    def __init__(self):
        self.board = [[Square(r,c) for c in range(COLS)] for r in range(ROWS)]
        self.populate_board(self.board)
        print(self.board)

    def populate_board(self, bo):
        for r in range(ROWS):
            for c in range(COLS):
                bo[r][c].piece = 0
                
