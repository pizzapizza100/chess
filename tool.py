class Tool:
    def __int__(self, x = 0 , y = 0, col = 0):
        self.posX = x
        self.posY = y
        self.color = col
        self.worth = None

    def can_move_to(self,x,y):
        # to do
        return False