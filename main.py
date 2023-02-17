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
    pass

def getPiece(x: int, y: int): # Use pixels
    pass

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
        else:
            mousepos = None

        if event.type == pygame.KEYDOWN:
            if event.unicode == "s":
                mouseX = 8
                mouseY = 8
                mousepos = None


######################## Appliance

####################### Game-Handling
    # Clicking (X, Y)
    if mousepos is not None:
        mouseX = convertValue("squares", mousepos[0])
        mouseY = convertValue("squares", mousepos[1])
    
####################### Graphics
    draw()
    clock.tick(fps)

####################### End of game loop
pygame.quit()
