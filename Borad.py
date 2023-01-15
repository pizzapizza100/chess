import Bishop,Queen,King,Knight,Rook,Pawn
from Tool import Color

class Borad:
    def __int__(self):
        self.board = [
            [Rook(col=Color.BLACK), Knight(col=Color.BLACK), Bishop(col=Color.BLACK), Queen(col=Color.BLACK),
             King(col=Color.BLACK), Bishop(col=Color.BLACK), Knight(col=Color.BLACK), Rook(col=Color.BLACK)],

            [Pawn(col=Color.BLACK),Pawn(col=Color.BLACK),Pawn(col=Color.BLACK),Pawn(col=Color.BLACK),
             Pawn(col=Color.BLACK),Pawn(col=Color.BLACK),Pawn(col=Color.BLACK),Pawn(col=Color.BLACK)],

            [None, None, None, None, None, None, None, None],

            [None, None, None, None, None, None, None, None],

            [None, None, None, None, None, None, None, None],

            [None, None, None, None, None, None, None, None],

            [Pawn(col=Color.WHITE), Pawn(col=Color.WHITE), Pawn(col=Color.WHITE), Pawn(col=Color.WHITE),
             Pawn(col=Color.WHITE), Pawn(col=Color.WHITE), Pawn(col=Color.WHITE), Pawn(col=Color.WHITE)],

            [Rook(col=Color.WHITE), Knight(col=Color.WHITE), Bishop(col=Color.WHITE), Queen(col=Color.WHITE),
             King(col=Color.WHITE), Bishop(col=Color.WHITE), Knight(col=Color.WHITE), Rook(col=Color.WHITE)],
        ]

