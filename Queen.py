import Tool
class Queen(Tool):
    def __int__(self):
        super(Queen, self).__init__(x = 0, y = 0, col = 0)
        self.worth = 9

    def can_move_to(self, x, y):
        # to do
        return False