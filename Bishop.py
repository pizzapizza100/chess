import Tool
class Bishop(Tool):
    def __int__(self):
        super(Bishop, self).__init__(x = 0, y = 0, col = 0)
        self.worth = 3

    def can_move_to(self, x, y):
        # to do
        return False