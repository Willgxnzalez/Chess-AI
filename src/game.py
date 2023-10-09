from const import *
import pygame
from board import Board

class Game:
    def __init__(self) -> None:
        self.theme = THEMES["navy-beige"]
        self.board = Board()


    def render_bg(self, surface: pygame.surface) -> None:
        for r in range(ROWS):
            for c in range(COLS):
                if (r+c) % 2 == 0:
                    color = self.theme[0]
                else:
                    color = self.theme[1]
                
                pygame.draw.rect(surface, color, (r * SQRSIZE, c * SQRSIZE, SQRSIZE, SQRSIZE))
