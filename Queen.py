from Tool import Tool

class Queen(Tool):
    def __int__(self,x = 0, y = 0, col = 0):
        super(Queen, self).__init__(x, y, col)
        self.worth = 9

    def can_move_to(self, x, y):
        # to do
        return False