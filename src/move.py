from square import Square

class Move:
    def __init__(self, origin: Square, dest: Square) -> None:
        self.origin = origin
        self.dest = dest

    def __eq__(self, other) -> bool:
        return self.origin == other.origin and self.dest == other.dest