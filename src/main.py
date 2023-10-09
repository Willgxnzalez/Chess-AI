from const import *
import sys
import pygame
from game import Game

class App:
    def __init__(self):
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.engine = Game()

    def mainloop(self):
        run = True
        while run:


            for E in pygame.event.get():
                if E.type == pygame.QUIT:
                    run = False


            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    app = App()
    app.mainloop()