from const import SQRSIZE

class Dragger:
    def __init__(self) -> None:
        self.mouse_pos = (0, 0)
        self.piece = None
        self.origin = None
        self.holding = False

    def update_mouse_pos(self, pos: tuple[int, int]) -> None:
        self.mouse_pos = pos

    def set_origin(self, pos: tuple[int,]) -> None:
        self.origin = (pos[1] // SQRSIZE, pos[0] // SQRSIZE)

    def get_board_pos(self):
        return self.mouse_pos[1] //SQRSIZE, self.mouse_pos[0] // SQRSIZE
    
    def grab_piece(self, piece):
        self.piece = piece
        self.holding = True