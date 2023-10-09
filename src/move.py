from square import Square

class Move:
    def __init__(self, src: Square, dest: Square) -> None:
        self.src = src
        self.dest = dest