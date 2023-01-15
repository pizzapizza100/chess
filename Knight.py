from Tool import Tool
class Knight(Tool):
    def __int__(self,x = 0, y = 0, col = 0):
        super(Knight, self).__init__(x, y , col)
        self.worth = 3

    def can_move_to(self, x, y):
        # to do
        return False