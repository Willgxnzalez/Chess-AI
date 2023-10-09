from piece import Piece

class Square:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.piece = None

    def set_piece(self, piece: Piece) -> None:
        self.piece = piece

    def has_piece(self) -> bool:
        return self.piece

    def __repr__(self):
        return f"Square({self.row}, {self.col})"