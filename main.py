import pygame
import time

#TODO: Need working on list
# Dont let pieces jump over each other
# Row 0 has some fancy shit going on, fix it
#
#TODO#######################


######################## Config
X = 400
Y = 400
fps = 60
color = (255,255,255)

######################## Nerdy shit
pygame.init()
scrn = pygame.display.set_mode((X, Y))
clock = pygame.time.Clock()
pygame.display.set_caption('Shess')

######################## "Obvious variables"
mouseX = 8
mouseY = 8
moveclick = False
clicked = False

######################## Load images
b_pawn = pygame.image.load(f"images/b_pawn.png")
b_knight = pygame.image.load(f"images/b_knight.png")
b_bishop = pygame.image.load(f"images/b_bishop.png")
b_rook = pygame.image.load(f"images/b_rook.png")
b_queen = pygame.image.load(f"images/b_queen.png")
b_king = pygame.image.load(f"images/b_king.png")
w_pawn = pygame.image.load(f"images/w_pawn.png")
w_knight = pygame.image.load(f"images/w_knight.png")
w_bishop = pygame.image.load(f"images/w_bishop.png")
w_rook = pygame.image.load(f"images/w_rook.png")
w_queen = pygame.image.load(f"images/w_queen.png")
w_king = pygame.image.load(f"images/w_king.png")
#Credit to these guys https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces/Standard_transparent

board = pygame.image.load(f"images/chessboard.png")

######################## Classes
class w_pawn1():
    status = True
    xpos = 0
    ypos = 6
    texture = "w_pawn"
class w_pawn2():
    status = True
    xpos = 1
    ypos = 6
    texture = "w_pawn"
class w_pawn3():
    status = True
    xpos = 2
    ypos = 6
    texture = "w_pawn"
class w_pawn4():
    status = True
    xpos = 3
    ypos = 6
    texture = "w_pawn"
class w_pawn5():
    status = True
    xpos = 4
    ypos = 6
    texture = "w_pawn"
class w_pawn6():
    status = True
    xpos = 5
    ypos = 6
    texture = "w_pawn"
class w_pawn7():
    status = True
    xpos = 6
    ypos = 6
    texture = "w_pawn"  
class w_pawn8():
    status = True
    xpos = 7
    ypos = 6
    texture = "w_pawn"
class w_rook1():
    status = True
    xpos = 0
    ypos = 7
    texture = "w_rook"
class w_rook2():
    status = True
    xpos = 7
    ypos = 7
    texture = "w_rook"
class w_bishop1():
    status = True
    xpos = 2
    ypos = 7
    texture = "w_bishop"
class w_bishop2():
    status = True
    xpos = 5
    ypos = 7
    texture = "w_bishop"
class w_knight1():
    status = True
    xpos = 1
    ypos = 7
    texture = "w_knight"
class w_knight2():
    status = True
    xpos = 6
    ypos = 7
    texture = "w_knight"
class w_king1():
    status = True
    xpos = 3
    ypos = 7
    texture = "w_king"
class w_queen1():
    status = True
    xpos = 4
    ypos = 7
    texture = "w_queen"

class b_pawn1():
    status = True
    xpos = 0
    ypos = 1
    texture = "b_pawn"
class b_pawn2():
    status = True
    xpos = 1
    ypos = 1
    texture = "b_pawn"
class b_pawn3():
    status = True
    xpos = 2
    ypos = 1
    texture = "b_pawn"
class b_pawn4():
    status = True
    xpos = 3
    ypos = 1
    texture = "b_pawn"
class b_pawn5():
    status = True
    xpos = 4
    ypos = 1
    texture = "b_pawn"
class b_pawn6():
    status = True
    xpos = 5
    ypos = 1
    texture = "b_pawn"
class b_pawn7():
    status = True
    xpos = 6
    ypos = 1
    texture = "b_pawn"
class b_pawn8():
    status = True
    xpos = 7
    ypos = 1
    texture = "b_pawn"
class b_rook1():
    status = True
    xpos = 0
    ypos = 0
    texture = "b_rook"
class b_rook2():
    status = True
    xpos = 7
    ypos = 0
    texture = "b_rook"
class b_bishop1():
    status = True
    xpos = 2
    ypos = 0
    texture = "b_bishop"
class b_bishop2():
    status = True
    xpos = 5
    ypos = 0
    texture = "b_bishop"
class b_knight1():
    status = True
    xpos = 1
    ypos = 0
    texture = "b_knight"
class b_knight2():
    status = True
    xpos = 6
    ypos = 0
    texture = "b_knight"
class b_king1():
    status = True
    xpos = 3
    ypos = 0
    texture = "b_king"
class b_queen1():
    status = True
    xpos = 4
    ypos = 0
    texture = "b_queen"

######################## Functions
#         Unit is always to, never from
def convertValue(unit, value): # Units: "pixels"/"squares" /\ Value: (just any value)
    if unit == "squares": # From pixels to squares
        return int(value / 50)
    elif unit == "pixels": # From squares to pixels
        return value * 50

def drawpieces():
    # Pawns
    if b_pawn1.status == True:
        scrn.blit(b_pawn, (convertValue("pixels", b_pawn1.xpos), convertValue("pixels", b_pawn1.ypos)))
    else:
        b_pawn1.xpos = 9
        b_pawn1.ypos = 9
    if b_pawn2.status == True:
        scrn.blit(b_pawn, (convertValue("pixels", b_pawn2.xpos), convertValue("pixels", b_pawn2.ypos)))
    else:
        b_pawn2.xpos = 9
        b_pawn2.ypos = 9
    if b_pawn3.status == True:
        scrn.blit(b_pawn, (convertValue("pixels", b_pawn3.xpos), convertValue("pixels", b_pawn3.ypos)))
    else:
        b_pawn3.xpos = 9
        b_pawn3.ypos = 9
    if b_pawn4.status == True:
        scrn.blit(b_pawn, (convertValue("pixels", b_pawn4.xpos), convertValue("pixels", b_pawn4.ypos)))
    else:
        b_pawn4.xpos = 9
        b_pawn4.ypos = 9
    if b_pawn5.status == True:
        scrn.blit(b_pawn, (convertValue("pixels", b_pawn5.xpos), convertValue("pixels", b_pawn5.ypos)))
    else:
        b_pawn5.xpos = 9
        b_pawn5.ypos = 9
    if b_pawn6.status == True:
        scrn.blit(b_pawn, (convertValue("pixels", b_pawn6.xpos), convertValue("pixels", b_pawn6.ypos)))
    else:
        b_pawn6.xpos = 9
        b_pawn6.ypos = 9
    if b_pawn7.status == True:
        scrn.blit(b_pawn, (convertValue("pixels", b_pawn7.xpos), convertValue("pixels", b_pawn7.ypos)))
    else:
        b_pawn7.xpos = 9
        b_pawn7.ypos = 9
    if b_pawn8.status == True:
        scrn.blit(b_pawn, (convertValue("pixels", b_pawn8.xpos), convertValue("pixels", b_pawn8.ypos)))
    else:
        b_pawn8.xpos = 9
        b_pawn8.ypos = 9
    if w_pawn1.status == True:
        scrn.blit(w_pawn, (convertValue("pixels", w_pawn1.xpos), convertValue("pixels", w_pawn1.ypos)))
    else:
        w_pawn1.xpos = 9
        w_pawn1.ypos = 9
    if w_pawn2.status == True:
        scrn.blit(w_pawn, (convertValue("pixels", w_pawn2.xpos), convertValue("pixels", w_pawn2.ypos)))
    else:
        w_pawn2.xpos = 9
        w_pawn2.ypos = 9
    if w_pawn3.status == True:
        scrn.blit(w_pawn, (convertValue("pixels", w_pawn3.xpos), convertValue("pixels", w_pawn3.ypos)))
    else:
        w_pawn3.xpos = 9
        w_pawn3.ypos = 9
    if w_pawn4.status == True:
        scrn.blit(w_pawn, (convertValue("pixels", w_pawn4.xpos), convertValue("pixels", w_pawn4.ypos)))
    else:
        w_pawn4.xpos = 9
        w_pawn4.ypos = 9
    if w_pawn5.status == True:
        scrn.blit(w_pawn, (convertValue("pixels", w_pawn5.xpos), convertValue("pixels", w_pawn5.ypos)))
    else:
        w_pawn5.xpos = 9
        w_pawn5.ypos = 9
    if w_pawn6.status == True:
        scrn.blit(w_pawn, (convertValue("pixels", w_pawn6.xpos), convertValue("pixels", w_pawn6.ypos)))
    else:
        w_pawn6.xpos = 9
        w_pawn6.ypos = 9
    if w_pawn7.status == True:
        scrn.blit(w_pawn, (convertValue("pixels", w_pawn7.xpos), convertValue("pixels", w_pawn7.ypos)))
    else:
        w_pawn7.xpos = 9
        w_pawn7.ypos = 9
    if w_pawn8.status == True:
        scrn.blit(w_pawn, (convertValue("pixels", w_pawn8.xpos), convertValue("pixels", w_pawn8.ypos)))
    else:
        w_pawn8.xpos = 9
        w_pawn8.ypos = 9

    # Rooks
    if b_rook1.status == True:
        scrn.blit(b_rook, (convertValue("pixels", w_rook1.xpos), convertValue("pixels", b_rook1.ypos)))
    else:
        b_rook1.xpos = 9
        b_rook1.ypos = 9
    if b_rook2.status == True:
        scrn.blit(b_rook, (convertValue("pixels", w_rook2.xpos), convertValue("pixels", b_rook2.ypos)))
    else:
        b_rook2.xpos = 9
        b_rook2.ypos = 9
    if w_rook1.status == True:
        scrn.blit(w_rook, (convertValue("pixels", w_rook1.xpos), convertValue("pixels", w_rook1.ypos)))
    else:
        w_rook1.xpos = 9
        w_rook1.ypos = 9
    if w_rook2.status == True:
        scrn.blit(w_rook, (convertValue("pixels", w_rook2.xpos), convertValue("pixels", w_rook2.ypos)))
    else:
        w_rook2.xpos = 9
        w_rook2.ypos = 9

    # Bishops
    if b_bishop1.status == True:
        scrn.blit(b_bishop, (convertValue("pixels", b_bishop1.xpos), convertValue("pixels", b_bishop1.ypos)))
    else:
        b_bishop1.xpos = 9
        b_bishop1.ypos = 9
    if b_bishop2.status == True:
        scrn.blit(b_bishop, (convertValue("pixels", b_bishop2.xpos), convertValue("pixels", b_bishop2.ypos)))
    else:
        b_bishop2.xpos = 9
        b_bishop2.ypos = 9
    if w_bishop1.status == True:
        scrn.blit(w_bishop, (convertValue("pixels", w_bishop1.xpos), convertValue("pixels", w_bishop1.ypos)))
    else:
        w_bishop1.xpos = 9
        w_bishop1.ypos = 9
    if w_bishop2.status == True:
        scrn.blit(w_bishop, (convertValue("pixels", w_bishop2.xpos), convertValue("pixels", w_bishop2.ypos)))
    else:
        w_bishop2.xpos = 9
        w_bishop2.ypos = 9

    # Knights
    if b_knight1.status == True:
        scrn.blit(b_knight, (convertValue("pixels", b_knight1.xpos), convertValue("pixels", b_knight1.ypos)))
    else:
        b_knight1.xpos = 9
        b_knight1.ypos = 9
    if b_knight2.status == True:
        scrn.blit(b_knight, (convertValue("pixels", b_knight2.xpos), convertValue("pixels", b_knight2.ypos)))
    else:
        b_knight2.xpos = 9
        b_knight2.ypos = 9
    if w_knight1.status == True:
        scrn.blit(w_knight, (convertValue("pixels", w_knight1.xpos), convertValue("pixels", w_knight1.ypos)))
    else:
        w_knight1.xpos = 9
        w_knight1.ypos = 9
    if w_knight2.status == True:
        scrn.blit(w_knight, (convertValue("pixels", w_knight2.xpos), convertValue("pixels", w_knight2.ypos)))
    else:
        w_knight2.xpos = 9
        w_knight2.ypos = 9

    # Kings
    if b_king1.status == True:
        scrn.blit(b_king, (convertValue("pixels", b_king1.xpos), convertValue("pixels", b_king1.ypos)))
    else:
        b_king1.xpos = 9
        b_king1.ypos = 9
    if w_king1.status == True:
        scrn.blit(w_king, (convertValue("pixels", w_king1.xpos), convertValue("pixels", w_king1.ypos)))
    else:
        w_king1.xpos = 9
        w_king1.ypos = 9

    # Queens
    if b_queen1.status == True:
        scrn.blit(b_queen, (convertValue("pixels", b_queen1.xpos), convertValue("pixels", b_queen1.ypos)))
    else:
        b_queen1.xpos = 9
        b_queen1.ypos = 9
    if w_queen1.status == True:
        scrn.blit(w_queen, (convertValue("pixels", w_queen1.xpos), convertValue("pixels", w_queen1.ypos)))
    else:
        w_queen1.xpos = 9
        w_queen1.ypos = 9

def draw():
    # Draw board
    scrn.blit(board, (0, 0))
    # Draw the pieces
    drawpieces()
    # Draw the selection square
    pygame.draw.rect(scrn, color, pygame.Rect(convertValue("pixels", mouseX), convertValue("pixels", mouseY), 50, 50), 2)
    # Update screen
    pygame.display.update()

def reset():
    pass

def canMove(piece: str, current: tuple, to: tuple): # Checks if a piece can move from one square to another
    tox = to[0]
    toy = to[1]
    currentx = current[0]
    currenty = current[1]
    currentColor = piece[0]
    toColor = getPiece(to[0], to[1])
    if toColor is None:
        toColor = "this is useless"
    toColor = toColor[0]
    toColor = toColor[0]

    movementStyle = piece
    piece = current[0]

    # Checks for own piece
    if currentColor[0] == toColor[0]:
        return False
    # Checks for other pieces

    # Bishops
    if movementStyle == "bishop":
        move = False
        index = -9
        for i in range(0, 16):
            index += 1
            if tox + index == currentx and toy + index == currenty:
                move = True
            if tox + index == currentx and toy - index == currenty:
                move = True
            if tox - index == currentx and toy + index == currenty:
                move = True
            if tox - index == currentx and toy - index == currenty:
                move = True
            if move == True:
                return True
        return False

    # Rooks
    elif movementStyle == "rook":
        if currentx == tox:
            return True
        elif currenty == toy:
            return True
        else: 
            return False
    
    # Queen
    elif movementStyle == "queen":
        # Stolen from Rook
        if currentx == tox:
            return True #TODO: Move piece
        elif currenty == toy:
            return True #TODO: Move piece

        # Stolen from Bishop
        move = False
        index = -9
        for i in range(0, 16):
            index += 1
            if tox + index == currentx and toy + index == currenty:
                move = True
            if tox + index == currentx and toy - index == currenty:
                move = True
            if tox - index == currentx and toy + index == currenty:
                move = True
            if tox - index == currentx and toy - index == currenty:
                move = True
            if move == True:
                return True #TODO: Move piece
        return False

    # King
    elif movementStyle == "king":
        if tox - 1 == currentx or tox + 1 == currentx:
            return True #TODO: move piece
        if toy - 1 == currenty or toy + 1 == currenty:
            return True #TODO: move piece
        else:
            return False

    elif movementStyle == "w_pawn" or movementStyle == "b_pawn":
        forward = "You broke sum shit"
        if movementStyle == "w_pawn":
            forward = 1
        if movementStyle == "b_pawn":
            forward = -1
        if toy + forward == currenty:
            if tox == currentx:
                return True
            elif to is not None:
                if tox - 1 == currentx or tox + 1 == currentx:
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False

    elif movementStyle == "knight":
        move = False
        if tox - 2 == currentx and toy - 1 == currenty:
            move = True
        if tox - 2 == currentx and toy + 1 == currenty:
            move = True
        if tox + 2 == currentx and toy - 1 == currenty:
            move = True
        if tox + 2 == currentx and toy + 1 == currenty:
            move = True
        if tox - 1 == currentx and toy - 2 == currenty:
            move = True
        if tox + 1 == currentx and toy - 2 == currenty:
            move = True
        if tox - 1 == currentx and toy + 2 == currenty:
            move = True
        if tox + 1 == currentx and toy + 2 == currenty:
            move = True
        if move == True:
            return True
        else:
            return False
    
def getPiece(x: int, y: int): # Use squares
    b_bishopp1 = ("b_bishop1", b_bishop1.xpos, b_bishop1.ypos, "bishop")
    b_bishopp2 = ("b_bishop2", b_bishop2.xpos, b_bishop2.ypos, "bishop")
    b_rookk1 = ("b_rook1", b_rook1.xpos, b_rook1.ypos, "rook")
    b_rookk2 = ("b_rook2", b_rook2.xpos, b_rook2.ypos, "rook")
    b_knightt1 = ("b_knight1", b_knight1.xpos, b_knight1.ypos, "knight")
    b_knightt2 = ("b_knight2", b_knight2.xpos, b_knight2.ypos, "knight")
    b_queenn1 = ("b_queen1", b_queen1.xpos, b_queen1.ypos, "queen")
    b_kingg1 = ("b_king1", b_king1.xpos, b_king1.ypos, "king")
    w_bishopp1 = ("w_bishop1", w_bishop1.xpos, w_bishop1.ypos, "bishop")
    w_bishopp2 = ("w_bishop2", w_bishop2.xpos, w_bishop2.ypos, "bishop")
    w_rookk1 = ("w_rook1", w_rook1.xpos, w_rook1.ypos, "rook")
    w_rookk2 = ("w_rook2", w_rook2.xpos, w_rook2.ypos, "rook")
    w_knightt1 = ("w_knight1", w_knight1.xpos, w_knight1.ypos, "knight")
    w_knightt2 = ("w_knight2", w_knight2.xpos, w_knight2.ypos, "knight")
    w_queenn1 = ("w_queen1", w_queen1.xpos, w_queen1.ypos, "queen")
    w_kingg1 = ("w_king1", w_king1.xpos, w_king1.ypos, "king")
    # pawns
    b_pawnn1 = ("b_pawn1", b_pawn1.xpos, b_pawn1.ypos, "b_pawn")
    b_pawnn2 = ("b_pawn2", b_pawn2.xpos, b_pawn2.ypos, "b_pawn")
    b_pawnn3 = ("b_pawn3", b_pawn3.xpos, b_pawn3.ypos, "b_pawn")
    b_pawnn4 = ("b_pawn4", b_pawn4.xpos, b_pawn4.ypos, "b_pawn")
    b_pawnn5 = ("b_pawn5", b_pawn5.xpos, b_pawn5.ypos, "b_pawn")
    b_pawnn6 = ("b_pawn6", b_pawn6.xpos, b_pawn6.ypos, "b_pawn")
    b_pawnn7 = ("b_pawn7", b_pawn7.xpos, b_pawn7.ypos, "b_pawn")
    b_pawnn8 = ("b_pawn8", b_pawn8.xpos, b_pawn8.ypos, "b_pawn")
    w_pawnn1 = ("w_pawn1", w_pawn1.xpos, w_pawn1.ypos, "w_pawn")
    w_pawnn2 = ("w_pawn2", w_pawn2.xpos, w_pawn2.ypos, "w_pawn")
    w_pawnn3 = ("w_pawn3", w_pawn3.xpos, w_pawn3.ypos, "w_pawn")
    w_pawnn4 = ("w_pawn4", w_pawn4.xpos, w_pawn4.ypos, "w_pawn")
    w_pawnn5 = ("w_pawn5", w_pawn5.xpos, w_pawn5.ypos, "w_pawn")
    w_pawnn6 = ("w_pawn6", w_pawn6.xpos, w_pawn6.ypos, "w_pawn")
    w_pawnn7 = ("w_pawn7", w_pawn7.xpos, w_pawn7.ypos, "w_pawn")
    w_pawnn8 = ("w_pawn8", w_pawn8.xpos, w_pawn8.ypos, "w_pawn")
    piecelist = [b_bishopp1, b_bishopp2, b_rookk1, b_rookk2, b_knightt1, b_knightt2, b_queenn1, b_kingg1, w_bishopp1, w_bishopp2, w_rookk1, w_rookk2, w_knightt1, w_knightt2, w_queenn1, w_kingg1, b_pawnn1, b_pawnn2, b_pawnn3, b_pawnn3, b_pawnn4, b_pawnn5, b_pawnn6, b_pawnn7, b_pawnn7, b_pawnn8, w_pawnn1, w_pawnn2, w_pawnn3, w_pawnn4, w_pawnn5, w_pawnn6, w_pawnn7, w_pawnn8]
    for i in piecelist:
        if i[1] == x and i[2] == y:
            return (i[0], i[3]) # [0] is name and [3] is movement-style
    return None

def nameToClass(name: str):
    if name == "b_bishop1":
        return b_bishop1
    if name == "b_bishop2":
        return b_bishop2
    if name == "w_bishop1":
        return w_bishop1
    if name == "w_bishop2":
        return w_bishop2

    if name == "b_rook1":
        return b_rook1
    if name == "b_rook2":
        return b_rook2
    if name == "w_rook1":
        return w_rook1
    if name == "w_rook2":
        return w_rook2

    if name == "b_knight1":
        return b_knight1
    if name == "b_knight2":
        return b_knight2
    if name == "w_knight1":
        return w_knight1
    if name == "w_knight2":
        return w_knight2

    if name == "b_queen1":
        return b_queen1
    if name == "w_queen1":
        return w_queen1

    if name == "b_king1":
        return b_king1
    if name == "w_king1":
        return w_king1

    if name == "b_pawn1":
        return b_pawn1
    if name == "b_pawn2":
        return b_pawn2
    if name == "b_pawn3":
        return b_pawn3
    if name == "b_pawn4":
        return b_pawn4
    if name == "b_pawn5":
        return b_pawn5
    if name == "b_pawn6":
        return b_pawn6
    if name == "b_pawn7":
        return b_pawn7
    if name == "b_pawn8":
        return b_pawn8
    if name == "w_pawn1":
        return w_pawn1
    if name == "w_pawn2":
        return w_pawn2
    if name == "w_pawn3":
        return w_pawn3
    if name == "w_pawn4":
        return w_pawn4
    if name == "w_pawn5":
        return w_pawn5
    if name == "w_pawn6":
        return w_pawn6
    if name == "w_pawn7":
        return w_pawn7
    if name == "w_pawn8":
        return w_pawn8

def move(piece, x: int, y: int):
    # Bishops
    if piece == b_bishop1:
        b_bishop1.xpos = x
        b_bishop1.ypos = y
    if piece == b_bishop2:
        b_bishop2.xpos = x
        b_bishop2.ypos = y
    if piece == w_bishop1:
        w_bishop1.xpos = x
        w_bishop1.ypos = y
    if piece == w_bishop2:
        w_bishop2.xpos = x
        w_bishop2.ypos = y

    # Rooks
    if piece == b_rook1:
        b_rook1.xpos = x
        b_rook1.ypos = y
    if piece == b_rook2:
        b_rook2.xpos = x
        b_rook2.ypos = y
    if piece == w_rook1:
        w_rook1.xpos = x
        w_rook1.ypos = y
    if piece == w_rook2:
        w_rook2.xpos = x
        w_rook2.ypos = y

    # Knights
    if piece == b_knight1:
        b_knight1.xpos = x
        b_knight1.ypos = y
    if piece == b_knight2:
        b_knight2.xpos = x
        b_knight2.ypos = y
    if piece == w_knight1:
        w_knight1.xpos = x
        w_knight1.ypos = y
    if piece == w_knight2:
        w_knight2.xpos = x
        w_knight2.ypos = y

    if piece == b_queen1:
        b_queen1.xpos = x
        b_queen1.ypos = y
    if piece == w_queen1:
        w_queen1.xpos = x
        w_queen1.ypos = y
    
    if piece == b_king1:
        b_king1.xpos = x
        b_king1.ypos = y
    if piece == w_king1:
        w_king1.xpos = x
        w_king1.ypos = y

    if piece == b_pawn1:
        b_pawn1.xpos = x
        b_pawn1.ypos = y
    if piece == b_pawn2:
        b_pawn2.xpos = x
        b_pawn2.ypos = y
    if piece == b_pawn3:
        b_pawn3.xpos = x
        b_pawn3.ypos = y
    if piece == b_pawn4:
        b_pawn4.xpos = x
        b_pawn4.ypos = y
    if piece == b_pawn5:
        b_pawn5.xpos = x
        b_pawn5.ypos = y
    if piece == b_pawn6:
        b_pawn6.xpos = x
        b_pawn6.ypos = y
    if piece == b_pawn7:
        b_pawn7.xpos = x
        b_pawn7.ypos = y
    if piece == b_pawn8:
        b_pawn8.xpos = x
        b_pawn8.ypos = y
    if piece == w_pawn1:
        w_pawn1.xpos = x
        w_pawn1.ypos = y
    if piece == w_pawn2:
        w_pawn2.xpos = x
        w_pawn2.ypos = y
    if piece == w_pawn3:
        w_pawn3.xpos = x
        w_pawn3.ypos = y
    if piece == w_pawn4:
        w_pawn4.xpos = x
        w_pawn4.ypos = y
    if piece == w_pawn5:
        w_pawn5.xpos = x
        w_pawn5.ypos = y
    if piece == w_pawn6:
        w_pawn6.xpos = x
        w_pawn6.ypos = y
    if piece == w_pawn7:
        w_pawn7.xpos = x
        w_pawn7.ypos = y
    if piece == w_pawn8:
        w_pawn8.xpos = x
        w_pawn8.ypos = y

def remove(piece):
    # Bishops
    if piece == b_bishop1:
        b_bishop1.status = False
    elif piece == b_bishop2:
        b_bishop2.status = False
    elif piece == w_bishop1:
        w_bishop1.status = False
    elif piece == w_bishop2:
        w_bishop2.status = False

    # Rooks
    elif piece == b_rook1:
        b_rook1.status = False
    elif piece == b_rook2:
        b_rook2.status = False
    elif piece == w_rook1:
        w_rook1.status = False
    elif piece == w_rook2:
        w_rook2.status = False

    # Knights
    elif piece == b_knight1:
        b_knight1.status = False
    elif piece == b_knight2:
        b_knight2.status = False
    elif piece == w_knight1:
        w_knight1.status = False
    elif piece == w_knight2:
        w_knight2.status = False

    elif piece == b_queen1:
        b_queen1.status = False
    elif piece == w_queen1:
        w_queen1.status = False
    
    elif piece == b_king1:
        b_king1.status = False
    elif piece == w_king1:
        w_king1.status = False

    elif piece == b_pawn1:
        b_pawn1.status = False
    elif piece == b_pawn2:
        b_pawn2.status = False
    elif piece == b_pawn3:
        b_pawn3.status = False
    elif piece == b_pawn4:
        b_pawn4.status = False
    elif piece == b_pawn5:
        b_pawn5.status = False
    elif piece == b_pawn6:
        b_pawn6.status = False
    elif piece == b_pawn7:
        b_pawn7.status = False
    elif piece == b_pawn8:
        b_pawn8.status = False
    elif piece == w_pawn1:
        w_pawn1.status = False
    elif piece == w_pawn2:
        w_pawn2.status = False
    elif piece == w_pawn3:
        w_pawn3.status = False
    elif piece == w_pawn4:
        w_pawn4.status = False
    elif piece == w_pawn5:
        w_pawn5.status = False
    elif piece == w_pawn6:
        w_pawn6.status = False
    elif piece == w_pawn7:
        w_pawn7.status = False
    elif piece == w_pawn8:
        w_pawn8.status = False

######################## Draw screen one time 
pygame.display.flip()
######################## Game loop
active = True
while (active):
    scrn.fill((0,0,0))
######################## Update variables

######################## Controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            active = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            mousepos = pygame.mouse.get_pos()
            clicked = True
        else:
            mousepos = None

        if event.type == pygame.KEYDOWN:
            if event.unicode == "s":
                mouseX = 8
                mouseY = 8
                mousepos = None
                moveclick = False

####################### Game-Handling
    # Clicking (X, Y)
    if mousepos is not None and clicked == True:
        if moveclick == True:
            piece = getPiece(mouseX, mouseY)
            oldmouseX = mouseX
            oldmouseY = mouseY
            mouseX = convertValue("squares", mousepos[0])
            mouseY = convertValue("squares", mousepos[1])
            if piece is not None:
                error = canMove(piece[1], (oldmouseX, oldmouseY), (mouseX, mouseY))
                if error == False: 
                    print("Invalid move")
                else: # Do the move
                    to = getPiece(mouseX, mouseY)
                    if to is not None:
                        remove(nameToClass(to[0]))
                    move(nameToClass(piece[0]), mouseX, mouseY)
                moveclick = False
                mouseX = 8
                mouseY = 8
                mousepos = None
                moveclick = False
        else:
            mouseX = convertValue("squares", mousepos[0])
            mouseY = convertValue("squares", mousepos[1])
            moveclick = True
    clicked = False
        
    
####################### Graphics
    draw()
    clock.tick(fps)

####################### End of game loop
pygame.quit()
