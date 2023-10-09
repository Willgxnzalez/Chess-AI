from const import *
import sys
import pygame
from game import Game

class App:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.engine = Game()

    def mainloop(self):
        engine = self.engine
        
        run = True
        while run:
            for E in pygame.event.get():
                if E.type == pygame.QUIT:
                    run = False
                if E.type == pygame.KEYDOWN:
                    if E.key == pygame.K_ESCAPE:
                        run = False

            engine.render_bg(self.win)
            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    app = App()
    app.mainloop()