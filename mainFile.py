# Tic Tac Toe gameI

import time
from Square import UNOCCUPIED, X_OCCUPIED, O_OCCUPIED
from Level import Level, squareList, NUM_OF_SQUARES
from Sprite import Sprite

# ------------------------------------------------------------------------------------------------------------------------------------------------- Setup

def setup():
    size(860, 733)
    this.surface.setTitle("Tic Tac Toe")
    
    global gameBoardImage
    global xImage
    global oImage
    global level
    global moveNumber
    global mouseXPos
    global mouseYPos
    global xWin
    global oWin
    global compOrPerson
    global completedStartMenu
    
    xWin = False
    oWin = False
    compOrPerson = False
    completedStartMenu = False
    mouseXPos = 0
    mouseYPos = 0
    gameBoardImage = loadImage("Tic_Tac_Toe_Board.png")
    xImage = loadImage("Tic_Tac_Toe_X.png")
    oImage = loadImage("Tic_Tac_Toe_O.png")
    level = Level(gameBoardImage)
    level.setSquares()
    moveNumber = 0
    
# ------------------------------------------------------------------------------------------------------------------------------------------------- Draw
    
def draw():
    global xWin
    global oWin
    global moveNumber
    global compOrPerson
    global completedStartMenu
    move = 0
    background(0)
    
    level.display()
    updatePieces()
    updateUI()
    if completedStartMenu == False:
        showStartMenu()
        
    if compOrPerson == "comp":
        if moveNumber % 2 != 0 and xWin == False and oWin == False:
            move = aiMove()
            moveNumber = Sprite(oImage, squareList[move].left + 1, squareList[move].top + 1, moveNumber).placePiece()

    if checkWin(squareList) != False:
        showEndMenu()
    
    if moveNumber == 9:
        showEndMenu()
    
    #updatePieces()

# ------------------------------------------------------------------------------------------------------------------------------------------------- Mouse/key pressed
                    
def mousePressed():
    global moveNumber
    global compOrPerson
    mouseXPos = mouseX
    mouseYPos = mouseY
    
    if xWin == False and oWin == False and completedStartMenu == True:
        if moveNumber % 2 == 0:
            moveNumber = Sprite(xImage, mouseXPos, mouseYPos, moveNumber).placePiece()
        else:
            moveNumber = Sprite(oImage, mouseXPos, mouseYPos, moveNumber).placePiece()
    
        
def keyPressed():
    global compOrPerson
    if key == ENTER:
        resetGame()
    if key == 'c':
        compOrPerson = "comp"
        resetGame()
    if key == 'p':
        compOrPerson = "person"
        resetGame()
        
# ------------------------------------------------------------------------------------------------------------------------------------------------- Update pieces

def updatePieces():
    for i in range(NUM_OF_SQUARES):
        if squareList[i].isOccupiedBy == X_OCCUPIED:
            Sprite(xImage, mouseXPos, mouseYPos, moveNumber).display(squareList[i].left, squareList[i].top)
            
        elif squareList[i].isOccupiedBy == O_OCCUPIED:
            Sprite(oImage, mouseXPos, mouseYPos, moveNumber).display(squareList[i].left, squareList[i].top)
            
# ------------------------------------------------------------------------------------------------------------------------------------------------- Check X and O win

def checkXWin(board):
    if board[0].isOccupiedBy == X_OCCUPIED and board[1].isOccupiedBy == X_OCCUPIED and board[2].isOccupiedBy == X_OCCUPIED:
        return True
    elif board[3].isOccupiedBy == X_OCCUPIED and board[4].isOccupiedBy == X_OCCUPIED and board[5].isOccupiedBy == X_OCCUPIED:
        return True
    elif board[6].isOccupiedBy == X_OCCUPIED and board[7].isOccupiedBy == X_OCCUPIED and board[8].isOccupiedBy == X_OCCUPIED:
        return True
    elif board[0].isOccupiedBy == X_OCCUPIED and board[3].isOccupiedBy == X_OCCUPIED and board[6].isOccupiedBy == X_OCCUPIED:
        return True
    elif board[1].isOccupiedBy == X_OCCUPIED and board[4].isOccupiedBy == X_OCCUPIED and board[7].isOccupiedBy == X_OCCUPIED:
        return True
    elif board[2].isOccupiedBy == X_OCCUPIED and board[5].isOccupiedBy == X_OCCUPIED and board[8].isOccupiedBy == X_OCCUPIED:
        return True
    elif board[0].isOccupiedBy == X_OCCUPIED and board[4].isOccupiedBy == X_OCCUPIED and board[8].isOccupiedBy == X_OCCUPIED:
        return True
    elif board[2].isOccupiedBy == X_OCCUPIED and board[4].isOccupiedBy == X_OCCUPIED and board[6].isOccupiedBy == X_OCCUPIED:
        return True
    else:
        return False
            
        
        
def checkOWin(board):
    if board[0].isOccupiedBy == O_OCCUPIED and board[1].isOccupiedBy == O_OCCUPIED and board[2].isOccupiedBy == O_OCCUPIED:
        return True
    elif board[3].isOccupiedBy == O_OCCUPIED and board[4].isOccupiedBy == O_OCCUPIED and board[5].isOccupiedBy == O_OCCUPIED:
        return True
    elif board[6].isOccupiedBy == O_OCCUPIED and board[7].isOccupiedBy == O_OCCUPIED and board[8].isOccupiedBy == O_OCCUPIED:
        return True
    elif board[0].isOccupiedBy == O_OCCUPIED and board[3].isOccupiedBy == O_OCCUPIED and board[6].isOccupiedBy == O_OCCUPIED:
        return True
    elif board[1].isOccupiedBy == O_OCCUPIED and board[4].isOccupiedBy == O_OCCUPIED and board[7].isOccupiedBy == O_OCCUPIED:
        return True
    elif board[2].isOccupiedBy == O_OCCUPIED and board[5].isOccupiedBy == O_OCCUPIED and board[8].isOccupiedBy == O_OCCUPIED:
        return True
    elif board[0].isOccupiedBy == O_OCCUPIED and board[4].isOccupiedBy == O_OCCUPIED and board[8].isOccupiedBy == O_OCCUPIED:
        return True
    elif board[2].isOccupiedBy == O_OCCUPIED and board[4].isOccupiedBy == O_OCCUPIED and board[6].isOccupiedBy == O_OCCUPIED:
        return True
    else:
        return False
    
# ------------------------------------------------------------------------------------------------------------------------------------------------- Check Win

def checkWin(board):
    global xWin
    global oWin
    if checkOWin(board):
        oWin = True
        return True
    elif checkXWin(board):
        xWin = True
        return True
    else:
        return False
    
# ------------------------------------------------------------------------------------------------------------------------------------------------- Update UI
    
def updateUI():
    fill(83)
    textSize(20)
    text("Press ENTER to restart \nPress 'c' to play computer \nPress 'p' to play a player", 555, 620)
    if moveNumber % 2 == 0:
        text("X's turn", 50, 700)
    else:
        text("O's turn", 50, 700)
    
# ------------------------------------------------------------------------------------------------------------------------------------------------- Start Menu
    
def showStartMenu():
    global completedStartMenu
    global compOrPerson
    background(100, 160, 160)
    textSize(40)
    fill(220, 220, 220)
    text("Press 'c' to play against the computer \n \n Press 'p' to play against a player", 95, 200)
    if compOrPerson != False:
        completedStartMenu = True

# ------------------------------------------------------------------------------------------------------------------------------------------------- End Menu

def showEndMenu():
    global xWin
    global oWin
    background(100, 160, 160)
    textSize(100)
    fill(220, 220, 220)
    if xWin == True:
        text("X Wins", 275, 200)

    elif oWin == True:
        text("O Wins.", 275, 200)
    
    else:
        text("It's a draw.", 210, 200)
    
    textSize(50)
    fill(255)
    text("ENTER to continue \n\n ESC to exit", 220, 400)
   
# ------------------------------------------------------------------------------------------------------------------------------------------------- AI

def aiMove():
    global oWin
    global xWin
    global moveNumber
    possibleMoves = [x for x, letter in enumerate(squareList) if letter.isOccupiedBy == UNOCCUPIED]
    move = 0
    
    for let in [O_OCCUPIED, X_OCCUPIED]:
        for i in possibleMoves:
            squareListCopy = squareList[:]
            squareListCopy[i].isOccupiedBy = let
            if checkXWin(squareListCopy) or checkOWin(squareListCopy):
                squareListCopy[i].isOccupiedBy = UNOCCUPIED
                return i
            else:
                squareListCopy[i].isOccupiedBy = UNOCCUPIED

    
    cornersOpen = []
    for i in possibleMoves:
        if i in [0, 2, 6, 8]:
            cornersOpen.append(i)
    
    
    if len(cornersOpen) > 0:
        randomNum = int(random(len(cornersOpen)))
        move = cornersOpen[randomNum]
        return move
    
    if 4 in possibleMoves:
        move = 4
        return move
        
    edgesOpen = []
    for i in possibleMoves:
        if i in [1, 3, 5, 7]:
            edgesOpen.append(i)
            
    if len(edgesOpen) > 0:
        randomNum = int(random(len(edgesOpen)))
        move = edgesOpen[randomNum]
        return move
    return move

# ------------------------------------------------------------------------------------------------------------------------------------------------- Reset game

def resetGame():
    global xWin
    global oWin
    global moveNumber
    level.setSquares()
    xWin = False
    oWin = False
    moveNumber = 0
