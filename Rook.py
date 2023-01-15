import Tool
class Rook(Tool):
    def __int__(self):
        super(Rook, self).__init__(x = 0, y = 0, col = 0)
        self.worth = 5

    def can_move_to(self, x, y):
        # to do
        return False