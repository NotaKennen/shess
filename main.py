import pygame
import time

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
# TODO: credit these guys https://commons.wikimedia.org/wiki/Category:SVG_chess_pieces/Standard_transparent

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
    scrn.blit(b_pawn, (convertValue("pixels", b_pawn1.xpos), convertValue("pixels", b_pawn1.ypos)))
    scrn.blit(b_pawn, (convertValue("pixels", b_pawn2.xpos), convertValue("pixels", b_pawn2.ypos)))
    scrn.blit(b_pawn, (convertValue("pixels", b_pawn3.xpos), convertValue("pixels", b_pawn3.ypos)))
    scrn.blit(b_pawn, (convertValue("pixels", b_pawn4.xpos), convertValue("pixels", b_pawn4.ypos)))
    scrn.blit(b_pawn, (convertValue("pixels", b_pawn5.xpos), convertValue("pixels", b_pawn5.ypos)))
    scrn.blit(b_pawn, (convertValue("pixels", b_pawn6.xpos), convertValue("pixels", b_pawn6.ypos)))
    scrn.blit(b_pawn, (convertValue("pixels", b_pawn7.xpos), convertValue("pixels", b_pawn7.ypos)))
    scrn.blit(b_pawn, (convertValue("pixels", b_pawn8.xpos), convertValue("pixels", b_pawn8.ypos)))
    scrn.blit(w_pawn, (convertValue("pixels", w_pawn1.xpos), convertValue("pixels", w_pawn1.ypos)))
    scrn.blit(w_pawn, (convertValue("pixels", w_pawn2.xpos), convertValue("pixels", w_pawn2.ypos)))
    scrn.blit(w_pawn, (convertValue("pixels", w_pawn3.xpos), convertValue("pixels", w_pawn3.ypos)))
    scrn.blit(w_pawn, (convertValue("pixels", w_pawn4.xpos), convertValue("pixels", w_pawn4.ypos)))
    scrn.blit(w_pawn, (convertValue("pixels", w_pawn5.xpos), convertValue("pixels", w_pawn5.ypos)))
    scrn.blit(w_pawn, (convertValue("pixels", w_pawn6.xpos), convertValue("pixels", w_pawn6.ypos)))
    scrn.blit(w_pawn, (convertValue("pixels", w_pawn7.xpos), convertValue("pixels", w_pawn7.ypos)))
    scrn.blit(w_pawn, (convertValue("pixels", w_pawn8.xpos), convertValue("pixels", w_pawn8.ypos)))

    # Rooks
    scrn.blit(w_rook, (convertValue("pixels", w_rook1.xpos), convertValue("pixels", w_rook1.ypos)))
    scrn.blit(w_rook, (convertValue("pixels", w_rook2.xpos), convertValue("pixels", w_rook2.ypos)))
    scrn.blit(b_rook, (convertValue("pixels", b_rook1.xpos), convertValue("pixels", b_rook1.ypos)))
    scrn.blit(b_rook, (convertValue("pixels", b_rook2.xpos), convertValue("pixels", b_rook2.ypos)))

    # Bishops
    scrn.blit(w_bishop, (convertValue("pixels", w_bishop1.xpos), convertValue("pixels", w_bishop1.ypos)))
    scrn.blit(w_bishop, (convertValue("pixels", w_bishop2.xpos), convertValue("pixels", w_bishop2.ypos)))
    scrn.blit(b_bishop, (convertValue("pixels", b_bishop1.xpos), convertValue("pixels", b_bishop1.ypos)))
    scrn.blit(b_bishop, (convertValue("pixels", b_bishop2.xpos), convertValue("pixels", b_bishop2.ypos)))

    # Knights
    scrn.blit(w_knight, (convertValue("pixels", w_knight1.xpos), convertValue("pixels", w_knight1.ypos)))
    scrn.blit(w_knight, (convertValue("pixels", w_knight2.xpos), convertValue("pixels", w_knight2.ypos)))
    scrn.blit(b_knight, (convertValue("pixels", b_knight1.xpos), convertValue("pixels", b_knight1.ypos)))
    scrn.blit(b_knight, (convertValue("pixels", b_knight2.xpos), convertValue("pixels", b_knight2.ypos)))

    # Kings
    scrn.blit(w_king, (convertValue("pixels", w_king1.xpos), convertValue("pixels", w_king1.ypos)))
    scrn.blit(b_king, (convertValue("pixels", b_king1.xpos), convertValue("pixels", b_king1.ypos)))

    # Queens
    scrn.blit(w_queen, (convertValue("pixels", w_queen1.xpos), convertValue("pixels", w_queen1.ypos)))
    scrn.blit(b_queen, (convertValue("pixels", b_queen1.xpos), convertValue("pixels", b_queen1.ypos)))

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

def move(piece: str, current: tuple, to: tuple): # Moves a piece from one square to another
    tox = to[0]
    toy = to[1]
    currentx = current[0]
    currenty = current[1]

    current = getPiece(current[0], current[1])
    to = getPiece(to[0], to[1])
    movementStyle = current[1]
    piece = current[0]

    if to is not None:
        pass # TODO: Remove piece from board

    # Bishops # TODO: fix
    if movementStyle == "bishop":
        index = -9
        for i in range(-8, 8):
            index += 1
            if tox == currentx + index:
                if toy == currenty + index:
                    pass # TODO: Move piece
                elif index >= 9:
                    return False
            elif index >= 9:
                return False

    # Rooks
    if movementStyle == "rook":
        if currentx == tox:
            pass #TODO: Move piece
        elif currenty == toy:
            pass #TODO: Move piece
        else: 
            return False
    
    # Queen
    if movementStyle == "queen":
        # Stolen from Rook
        if currentx == tox:
            pass #TODO: Move piece
        elif currenty == toy:
            pass #TODO: Move piece

        # Stolen from Bishop TODO: fix
        index = -9
        for i in range(-8, 8):
            index += 1
            if tox == currentx + index:
                if toy == currenty + index:
                    pass # TODO: Move piece
                elif index >= 9:
                    return False
            elif index >= 9:
                return False

    # King
    if movementStyle == "king":
        if tox - 1 == currentx or tox + 1 == currentx:
            pass #TODO: move piece
        if toy - 1 == currenty or toy + 1 == currenty:
            pass #TODO: move piece
        else:
            return False

    if movementStyle == "w_pawn" or movementStyle == "b_pawn":
        forward = "You broke sum shit"
        if movementStyle == "w_pawn":
            forward = 1
        if movementStyle == "b_pawn":
            forward = -1
        if toy + forward == currenty:
            if tox == currentx:
                pass # TODO: Move piece
            elif to is not None:
                if tox - 1 == currentx or tox + 1 == currentx:
                    pass # TODO: Move piece
                else:
                    return False
            else:
                return False
        else:
            return False

    if movementStyle == "knight":
        pass
    

def getPiece(x: int, y: int): # Use squares
    if True == True:
        b_bishopp1 = ("b_bishop1", b_bishop1.xpos, b_bishop1.ypos, "bishop")
        b_bishopp2 = ("b_bishop2", b_bishop2.xpos, b_bishop2.ypos, "bishop")
        b_rookk1 = ("b_rook1", b_rook1.xpos, b_rook1.ypos, "rook")
        b_rookk2 = ("b_rook2", b_rook2.xpos, b_rook2.ypos, "rook")
        b_knightt1 = ("b_knight1", b_knight1.xpos, b_knight1.ypos, "knight")
        b_knightt2 = ("b_knight1", b_knight1.xpos, b_knight2.ypos, "knight")
        b_queenn1 = ("b_queen1", b_queen1.xpos, b_queen1.ypos, "queen")
        b_kingg1 = ("b_king1", b_king1.xpos, b_king1.ypos, "king")
        w_bishopp1 = ("w_bishop1", w_bishop1.xpos, w_bishop1.ypos, "bishop")
        w_bishopp2 = ("w_bishop2", w_bishop2.xpos, w_bishop2.ypos, "bishop")
        w_rookk1 = ("w_rook1", w_rook1.xpos, w_rook1.ypos, "rook")
        w_rookk2 = ("w_rook2", w_rook2.xpos, w_rook2.ypos, "rook")
        w_knightt1 = ("w_knight1", w_knight1.xpos, w_knight1.ypos, "knight")
        w_knightt2 = ("w_knight1", w_knight1.xpos, w_knight2.ypos, "knight")
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
                error = move(piece[0], (oldmouseX, oldmouseY), (mouseX, mouseY))
                if error == False:
                    print("Invalid move")
                else: # TODO: Remove on non-debug
                    print("VALID MOVE")
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
