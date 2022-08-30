from Level import squareList, NUM_OF_SQUARES
from Square import UNOCCUPIED, X_OCCUPIED, O_OCCUPIED

class Sprite:
    def __init__(self, img, mouseXPos, mouseYPos, moveNumber):
        self.charImg = img
        self.mouseXPos = mouseXPos
        self.mouseYPos = mouseYPos
        self.topLeftXPos = 0
        self.topLeftYPos = 0
        self.moveNumber = moveNumber
    
    def display(self, x, y):
        image(self.charImg, x, y)
        
        
    def placePiece(self):
        for i in range(NUM_OF_SQUARES):
            # Check if the mouse position colides with any of the squares. 
            if self.mouseYPos < squareList[i].bottom and self.mouseYPos > squareList[i].top and self.mouseXPos < squareList[i].right and self.mouseXPos > squareList[i].left and squareList[i].isOccupiedBy == UNOCCUPIED:
                self.display(squareList[i].left, squareList[i].top)
                if self.moveNumber % 2 == 0:
                    squareList[i].isOccupiedBy = X_OCCUPIED
                    
                elif self.moveNumber % 2 != 0:
                    squareList[i].isOccupiedBy = O_OCCUPIED
                self.moveNumber += 1
                    
        return self.moveNumber
