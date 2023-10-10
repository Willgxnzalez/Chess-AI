from const import *
from square import Square
from piece import *
from move import Move

class Board(list):
    def __init__(self) -> None:
        super().__init__([Square(r,c) for c in range(COLS)] for r in range(ROWS))

    def in_range(self, *indices):
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

        self[4][4].set_piece(Knight(color))

    def get_straights(self, row, col) -> list[tuple[int, int]]:
        straights = []
        # up
        for i in range(1, row+1):
            straights.append((row-i, col))
            if self[row-i][col].has_piece(): break
        # right
        for i in range(1, COLS-col):
            straights.append((row, col+i))
            if self[row][col+i].has_piece(): break
        # down
        for i in range(1, ROWS-row):
            straights.append((row+i, col))
            if self[row+i][col].has_piece(): break
        # left
        for i in range(1, col+1):
            straights.append((row, col-i))
            if self[row][col-i].has_piece(): break
        return straights
    
    def get_diagonals(self, row, col) -> list[tuple[int, int]]:
        diagonals = []
        # top-left
        for i in range(1, min(row, col)+1):
            diagonals.append((row - i, col - i))
            if self[row-i][col-i].has_piece(): break
        # top-right 
        for i in range(1, min(row, COLS-col-1)+1):
            diagonals.append((row - i, col + i))
            if self[row-i][col+i].has_piece(): break
        # bottom-right
        for i in range(1, min(ROWS-row-1, COLS-col-1)+1):
            diagonals.append((row + i, col + i))
            if self[row+i][col+i].has_piece(): break
        # bottom-left
        for i in range(1, min(ROWS-row-1, col)+1): 
            diagonals.append((row + i, col - i))
            if self[row+i][col-i].has_piece(): break
        return diagonals
        
    def get_valid_moves(self, sq: Square) -> None:
        piece, row, col = sq.piece, sq.row, sq.col
    
        if piece.rank == "pawn":
            viable_moves = []
            # forward
            max_row = 3 if not piece.moved else 2
            for i in range(1, max_row):
                viable_moves.append((row + (i * piece.direction), col))
            # adjacent

            
        elif piece.rank == "knight":
            viable_moves = [(row-2, col+1), (row-1, col+2), (row+1, col+2), (row+2, col+1),
                               (row+2, col-1), (row+1, col-2), (row-1, col-2), (row-2, col-1)]
        elif piece.rank == "rook":
            viable_moves = self.get_straights(row, col)

        elif piece.rank == "bishop":
            viable_moves = self.get_diagonals(row, col)

        elif piece.rank == "queen":
            viable_moves = self.get_diagonals(row, col) + self.get_straights(row, col)
        
        elif piece.rank == "king":
            viable_moves = [(row-1, col-1), (row-1, col), (row-1, col+1),
                            (row, col - 1), ( row, col ), (row, col + 1),
                            (row+1, col-1), (row+1, col), (row+1, col+1)]

        for r, c in viable_moves:
            if self.in_range(r, c):
                if not self[r][c].has_piece() or self[r][c].is_rival(piece):
                    piece.add_move(Move(Square(row, col), Square(r, c)))

