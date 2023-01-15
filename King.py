from Tool import Tool
class King(Tool):
    def __int__(self,x = 0, y = 0, col = 0):
        super(King, self).__init__(x, y, col)
        self.worth = None

    def can_move_to(self, x, y):
        # to do
        return False