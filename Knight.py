import Tool
class Knight(Tool):
    def __int__(self):
        super(Knight, self).__init__(x = 0, y = 0, col = 0)
        self.worth = 3

    def can_move_to(self, x, y):
        # to do
        return False