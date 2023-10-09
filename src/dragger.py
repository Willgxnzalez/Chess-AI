from const import SQRSIZE

class Dragger:
    def __init__(self) -> None:
        self.mouse_pos = (0, 0)
        self.piece = None
        self.origin = (0, 0)

    def update_mouse_pos(self, pos: tuple[int, int]) -> None:
        self.mouse_pos = pos

    def set_origin(self, pos: tuple[int,]) -> None:
        self.origin = pos

    def get_board_pos(self):
        return self.mouse_pos[1] //SQRSIZE, self.mouse_pos[0] // SQRSIZE