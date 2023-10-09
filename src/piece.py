from typing import Any
from const import *
import pygame
import os

class Piece:
    def __init__(self, rank: str, color: str, value: int) -> None:
        self.rank = rank
        self.color = color
        self.value = value * (-1 if self.color == "white" else 1)
        self.texture = pygame.transform.scale(pygame.image.load(os.path.join(f"assets/images/imgs-80px/{self.color}_{self.rank}.png")), (SQRSIZE, SQRSIZE))

class Pawn(Piece):
    def __init__(self, rank: str, color: str, value: int) -> None:
        self.direction = -1 if color
        super().__init__(rank, color, value)
        