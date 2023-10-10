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
            for E in pygame.event.get():
                if E.type == pygame.QUIT:
                    run = False

                if E.type == pygame.KEYDOWN:
                    if E.key == pygame.K_ESCAPE:
                        run = False

                if E.type == pygame.MOUSEBUTTONDOWN:
                    dragger.update_mouse_pos(E.pos)

                    row, col = dragger.get_board_pos()
                    selected_square = board[row][col]

                    if selected_square.has_piece():
                        board.get_valid_moves(selected_square.piece, row, col)
                        dragger.set_origin(selected_square)
                        dragger.grab_piece(selected_square.piece)

                if E.type == pygame.MOUSEMOTION:
                    if dragger.holding:
                        dragger.update_mouse_pos(E.pos)

                if E.type == pygame.MOUSEBUTTONUP:
                    dragger.update_mouse_pos(E.pos)

                    row, col = dragger.get_board_pos()
                    selected_square = board[row][col]

                    move_attempt = board.create_move(dragger.get_origin(), selected_square)
                    if board.valid_move(dragger.piece, move_attempt):
                        print("Valid move:", move_attempt)

                    dragger.release_piece()
            
            engine.render_bg(self.win)

            if dragger.holding:
                engine.render_piece_moves(self.win)
                engine.render_pieces(self.win)
                engine.render_held_piece(self.win)
            else:
                engine.render_pieces(self.win)
            pygame.display.update()

        pygame.quit()
        sys.exit()


if __name__ == "__main__":
    app = App()
    app.mainloop()