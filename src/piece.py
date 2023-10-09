from const import *
import pygame
import os

class Piece:
    def __init__(self, rank: str, color: str, value: float) -> None:
        self.rank = rank
        self.color = color
        self.value = value * (-1 if self.color == "white" else 1)
        self.texture = pygame.image.load(os.path.join(f"assets/images/imgs-80px/{self.color}_{self.rank}.png"))
        self.rect = None

    def set_rect(self, rect: pygame.rect) -> None:
        self.rect = rect

class Pawn(Piece):
    def __init__(self, color: str) -> None:
        self.direction = -1 if color == "white" else 1
        super().__init__("pawn", color, 1.0)

    def candidate_moves(self, row, col):
        pass

class Rook(Piece):
    def __init__(self, color: str) -> None:
        self.direction = -1 if color == "white" else 1
        super().__init__("rook", color, 5.0)

    def candidate_moves(self, row, col):
        pass

class Knight(Piece):
    def __init__(self, color: str) -> None:
        self.direction = -1 if color == "white" else 1
        super().__init__("knight", color, 3.0)

    def candidate_moves(self, row, col):
       return ((row-2, col+1),
                (row-1, col+2),
                (row+1, col+2),
                (row+2, col+1),
                (row+2, col-1),
                (row+1, col-2),
                (row-1, col-2),
                (row-2, col-2))

class Bishop(Piece):
    def __init__(self, color: str) -> None:
        self.direction = -1 if color == "white" else 1
        super().__init__("bishop", color, 3.1)

    def candidate_moves(self, row, col):
        pass

class Queen(Piece):
    def __init__(self, color: str) -> None:
        self.direction = -1 if color == "white" else 1
        super().__init__("queen", color, 9.0)

    def candidate_moves(self, row, col):
        pass

class King(Piece):
    def __init__(self, color: str) -> None:
        self.direction = -1 if color == "white" else 1
        super().__init__("king", color, 5000.0)

    def candidate_moves(self, row, col):
        pass