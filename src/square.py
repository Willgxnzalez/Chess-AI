class Square:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col
        self.piece = None

    def __repr__(self):
        return f"Square({self.row}, {self.col})"