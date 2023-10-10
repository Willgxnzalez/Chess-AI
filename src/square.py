from piece import Piece

class Square:
    def __init__(self, row: int, col: int, piece: Piece = None) -> None:
        self.row = row
        self.col = col
        self.piece = piece

    def set_piece(self, piece: Piece) -> None:
        self.piece = piece

    def has_piece(self) -> bool:
        return self.piece != None
    
    def rivals(self, other: Piece) -> bool:
        """returns true if the piece in this square rivals other"""
        if self.piece:
            return self.piece.color != other.color

    def __eq__(self, other) -> bool:
        return self.piece == other.piece and self.row == other.row and self.col == other.col

    def __repr__(self):
        return f"Square({self.row}, {self.col})"