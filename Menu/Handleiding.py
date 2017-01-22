import pygame
import sys


def story():

    redSquare = pygame.image.load('Story.png').convert()
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels()

def regels():

    redSquare = pygame.image.load('Naamloos.png').convert()
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels2()

def regels2():

    redSquare = pygame.image.load('Regels2.png').convert()
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels3()
def regels3():

    redSquare = pygame.image.load('Regels3.png').convert()
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels4()

def regels4():

    redSquare = pygame.image.load('surprisekaart.png').convert()
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels5()

def regels5():

    redSquare = pygame.image.load('Questregels2.png').convert()
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels6()

def regels6():

    redSquare = pygame.image.load('Powerupregels.png').convert()
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels7()

def regels7():

    redSquare = pygame.image.load('Powerupregels2.png').convert()
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels8()
def regels8():

    redSquare = pygame.image.load('Battleregels.png').convert()
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels9()

def regels9():

    redSquare = pygame.image.load('Battleregels2.png').convert()
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels10()

def regels10():

    redSquare = pygame.image.load('Battleregels3.png').convert()
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    print("hi")

def regels11():

    redSquare = pygame.image.load('Howtoplay.png').convert()
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels12()

def regels12():

    redSquare = pygame.image.load('Howtoplay2.png').convert()
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels13()


def regels13():

    redSquare = pygame.image.load('Howtoplay3.png').convert()
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels14()

def regels14():

    redSquare = pygame.image.load('Howtoplay4.png').convert()
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels15()


def regels15():

    redSquare = pygame.image.load('Howtoplay5.png').convert()
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    story()