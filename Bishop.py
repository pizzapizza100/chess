from Tool import Tool

class Bishop(Tool):
    def __int__(self,x = 0, y = 0, col = 0):
        super(Bishop, self).__init__(x=x , y=y , col=col)
        self.worth = 3

    def can_move_to(self, x, y):
        # to do
        return False