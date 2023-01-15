import Tool
class King(Tool):
    def __int__(self):
        super(King, self).__init__(x = 0, y = 0, col = 0)
        self.worth = None

    def can_move_to(self, x, y):
        # to do
        return False