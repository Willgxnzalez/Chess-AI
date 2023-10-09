class Piece:
    def __init__(self, rank: str, color: str, value: int) -> None:
        self.rank = rank
        self.color = color
        self.value = value * (-1 if self.color == "white" else 1)

