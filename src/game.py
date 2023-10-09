from const import *
import pygame
from board import Board
from dragger import Dragger

class Game:
    def __init__(self) -> None:
        self.theme = THEMES["navy-beige"]
        self.dragger = Dragger()
        self.board = Board()
        self.board.populate_board("white")
        self.board.populate_board("black")



    def render_bg(self, surface: pygame.surface) -> None:
        for r in range(ROWS):
            for c in range(COLS):
                if (r+c) % 2 == 0:
                    color = self.theme[0]
                else:
                    color = self.theme[1]
                
                pygame.draw.rect(surface, color, (r * SQRSIZE, c * SQRSIZE, SQRSIZE, SQRSIZE))

    def render_pieces(self, surface: pygame.surface) -> None:
        for r in range(ROWS):
            for c in range(COLS):
                sqr = self.board[r][c]
                if sqr.has_piece():

                    texture = pygame.transform.smoothscale(sqr.piece.texture, (SQRSIZE, SQRSIZE))
                    surface.blit(texture, (c*SQRSIZE, r*SQRSIZE))
