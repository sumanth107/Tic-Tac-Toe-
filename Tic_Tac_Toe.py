#@uthor : Sumanth Nethi
import pygame

pygame.init()

screen = pygame.display.set_mode((500, 500))
pygame.display.set_caption('TIC TAC TOE')
font = pygame.font.Font('freesansbold.ttf', 40)


black = (0, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
grey = (192, 192, 192)
dark_grey = (48, 48, 48)
red = (255, 0, 0)

XO = 'X'
game = [[None, None, None],
        [None, None, None],
        [None, None, None]]

board = pygame.Surface((460, 460))
board.fill(dark_grey)
row = 0
col = 0
winner = None
count = 0
for i in range(1, 3):
    pygame.draw.rect(board, grey, (0, 150 * i, 460, 5))
    pygame.draw.rect(board, grey, (150 * i, 0, 5, 460))

running = True


def drawO(tuple):
    O = pygame.Surface((140, 140))
    O.fill(dark_grey)
    pygame.draw.circle(O, red, (70, 70), 70, 7)
    screen.blit(O, tuple)


def drawX(tuple):
    X = pygame.Surface((140, 140))
    X.fill(dark_grey)
    pygame.draw.line(X, green, (10, 10), (140, 140), 7)
    pygame.draw.line(X, green, (140, 10), (10, 140), 7)
    screen.blit(X, tuple)


grid = [[(20, 20), (175, 20), (330, 20)],
        [(20, 175), (175, 175), (330, 175)],
        [(20, 330), (175, 330), (330, 330)]]


def gridpos(x, y):
    row = 0
    col = 0
    if y < 175:
        row = 0
    elif y < 330:
        row = 1
    else:
        row = 2
    if x < 175:
        col = 0
    elif x < 330:
        col = 1
    else:
        col = 2
    return (row, col)


def putPeice(row, col, piece):
    game[row][col] = piece


def wincheck(board):
    global game, grid, winner, count

    for i in range(0, 3):
        if (game[i][0] == game[i][1] == game[i][2]) and (game[i][0] is not None):
            winner = game[row][0]
            pygame.draw.line(board, black, (0, (i + 1) * 170 - 90), (500, (i + 1) * 170 - 90), 10)
            break

    for j in range(0, 3):
        if (game[0][j] == game[1][j] == game[2][j]) and (game[0][j] is not None):
            winner = game[0][j]
            pygame.draw.line(board, black, ((j + 1) * 170 - 90, 0), ((j + 1) * 170 - 90, 500), 10)
            break

    if (game[0][0] == game[1][1] == game[2][2]) and (game[0][0] is not None):
        winner = game[0][0]
        pygame.draw.line(board, black, (20, 20), (500, 500), 10)

    if (game[0][2] == game[1][1] == game[2][0]) and (game[0][2] is not None):
        winner = game[0][2]
        pygame.draw.line(board, black, (500, 0), (0, 500), 10)
    if winner is not None:
        show = font.render(str(winner) + ' WINS', True, white)
        screen.blit(show, (160,220))
    if count == 9 and winner is None:
        tie = font.render('MATCH TIED', True, white)
        screen.blit(tie, (120,220))


while running:
    screen.fill(black)
    screen.blit(board, (20, 20))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type is pygame.MOUSEBUTTONDOWN:
            count += 1
            (mouseX, mouseY) = pygame.mouse.get_pos()
            (row, col) = gridpos(mouseX, mouseY)
            x = row
            y = col
            if game[row][col] == 'X' or game[row][col] == 'O':
                continue
            else:
                putPeice(row, col, XO)
            if XO == 'X':
                XO = 'O'
            else:
                XO = 'X'
    for i in range(3):
        for j in range(3):
            if game[i][j] == 'X':
                drawX(grid[i][j])
            if game[i][j] == 'O':
                drawO(grid[i][j])
    wincheck(screen)
    pygame.display.update()
