import Tool
class Pawn(Tool):
    def __int__(self):
        super(Pawn, self).__init__(x = 0, y = 0, col = 0)
        self.worth = 1

    def can_move_to(self, x, y):
        # to do
        return False