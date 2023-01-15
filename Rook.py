from Tool import Tool
class Rook(Tool):
    def __int__(self,x = 0, y = 0, col = 0):
        super(Rook, self).__init__(x, y , col)
        self.worth = 5

    def can_move_to(self, x, y):
        # to do
        return False