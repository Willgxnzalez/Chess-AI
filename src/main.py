from const import *
import sys
import pygame
from game import Game

class App:
    def __init__(self) -> None:
        self.win = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()
        self.engine = Game()

    def mainloop(self) -> None:
        engine = self.engine
        run = True
        while run:
            self.clock.tick(FPS)
            for E in pygame.event.get():
                if E.type == pygame.QUIT:
                    run = False
                if E.type == pygame.KEYDOWN:
                    if E.key == pygame.K_ESCAPE:
                        run = False

                if E.type == pygame.MOUSEMOTION:
                    pass

            engine.render_bg(self.win)
            engine.render_pieces(self.win)

            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    app = App()
    app.mainloop()