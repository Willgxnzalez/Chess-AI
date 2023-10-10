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
                    if sqr.piece != self.dragger.piece:
                        texture = pygame.transform.smoothscale(sqr.piece.texture, (SQRSIZE, SQRSIZE))
                        surface.blit(texture, (c*SQRSIZE, r*SQRSIZE))
    
    def render_held_piece(self, surface: pygame.surface) -> None:
        upscaled_texture = pygame.transform.smoothscale(self.dragger.piece.texture, (SQRSIZE * 1.5, SQRSIZE * 1.5))
        texture_center = upscaled_texture.get_rect(center=self.dragger.mouse_pos)
        surface.blit(upscaled_texture, texture_center)

    def render_piece_moves(self, surface) -> None:
        if self.dragger.holding:
            for move in self.dragger.piece.get_moves():
                # create transparent surface for highlight
                highlight = pygame.Surface((SQRSIZE, SQRSIZE))
                highlight.fill(self.theme[2])
                highlight.set_alpha(130)

                surface.blit(highlight, (move.dest.col * SQRSIZE, move.dest.row * SQRSIZE))


                