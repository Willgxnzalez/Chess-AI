from const import SQRSIZE
import pygame
from square import Square

class Dragger:
    def __init__(self) -> None:
        self.mouse_pos = (0, 0)
        self.piece = None
        self.origin = None
        self.holding = False

    def update_mouse_pos(self, pos: tuple[int, int]) -> None:
        self.mouse_pos = pos

    def set_origin(self, origin: Square) -> None:
        self.origin = origin

    def get_origin(self) -> Square:
        return self.origin

    def get_board_pos(self) -> tuple[int, int]:
        return self.mouse_pos[1] //SQRSIZE, self.mouse_pos[0] // SQRSIZE
    
    def grab_piece(self, piece) -> None:
        self.piece = piece
        self.holding = True

    def release_piece(self) -> None:
        self.piece.clear_moves()
        self.piece = None
        self.holding = False


