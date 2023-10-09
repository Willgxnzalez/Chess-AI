from const import *
from square import Square
from piece import Piece

class Board:
    def __init__(self) -> None:
        self.sqrs = [[Square(r,c) for c in range(COLS)] for r in range(ROWS)]
        self.populate_board(self.sqrs)

    def populate_board(self, sqrs: list) -> None:
        for r in range(ROWS):
            for c in range(COLS):
                sqrs[r][c].piece = Piece("rook", "white", 9)
                
