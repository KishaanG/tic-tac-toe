UNOCCUPIED = 0
X_OCCUPIED = 1
O_OCCUPIED = 2

class Square:
    def __init__(self, left, right, top, bottom, isOccupiedBy):
        self.left = left
        self.right = right
        self.top = top
        self.bottom = bottom
        self.isOccupiedBy = isOccupiedBy
        
    def display(self):
        fill(100, 100, 100, 100)
        rect(self.left, self.top, self.right-self.left, self.bottom-self.top)
