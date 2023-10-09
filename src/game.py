from const import *
import pygame

class Game:
    def __init__(self):
        self.theme = COLORS["navy-beige"]

    def render_bg(self, surface):
        for r in range(ROWS):
            for c in range(COLS):
                if (r+c) % 2 == 0:
                    color = self.theme[0]
                else:
                    color = self.theme[1]
                
                pygame.draw.rect(surface, color, (r * SQRSIZE, c * SQRSIZE, SQRSIZE, SQRSIZE))
