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
        board = engine.board
        dragger = engine.dragger

        run = True
        while run:
            self.clock.tick(FPS)

            engine.render_bg(self.win)

            for E in pygame.event.get():
                if E.type == pygame.QUIT:
                    run = False
                if E.type == pygame.KEYDOWN:
                    if E.key == pygame.K_ESCAPE:
                        run = False

                if E.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse_pos(E.pos)

                    row, col = dragger.get_board_pos()
                    clicked_square = board[row][col]

                    if clicked_square.has_piece():
                        dragger.set_origin(E.pos)
                        dragger.grab_piece(clicked_square.piece)
                    
                    print(dragger.holding)

                if E.type == pygame.MOUSEMOTION:
                    if dragger.holding:
                        dragger.update_mouse_pos(E.pos)
                        engine.render_held_piece(self.win)


            
            engine.render_pieces(self.win)

            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    app = App()
    app.mainloop()