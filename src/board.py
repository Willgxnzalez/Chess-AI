from const import *
from square import Square
from piece import *

class Board(list):
    def __init__(self) -> None:
        super().__init__([Square(r,c) for c in range(COLS)] for r in range(ROWS))

    @staticmethod
    def in_range(*indices):
        for i in indices:
            if i < 0 or i > 7:
                return False
        return True
    
    def populate_board(self, color) -> None:
        others, pawns = (0, 1) if color == "black" else (7, 6)
        
        for c in range(COLS):
            self[pawns][c].set_piece(Pawn(color))

        self[others][0].set_piece(Rook(color))
        self[others][1].set_piece(Knight(color))
        self[others][2].set_piece(Bishop(color))
        self[others][3].set_piece(Queen(color))
        self[others][4].set_piece(King(color))
        self[others][5].set_piece(Bishop(color))
        self[others][6].set_piece(Knight(color))
        self[others][7].set_piece(Rook(color))

    def calc_valid_moves(self):
        pass


