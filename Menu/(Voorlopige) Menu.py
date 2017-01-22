import pygame
import Manual as M
import Game as dm
import sys
pygame.init()
def music():
    if True:
        pygame.mixer.music.load("music.mp3")
        pygame.mixer.music.play(loops = 999, start = 0.0)
        pygame.mixer.music.set_volume(0.2)
def Hoofdmenu():
    redSquare = pygame.image.load('MENU.png')
    white = (255,255,255)
    w = 700
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))
    x = 0
    y = 0
    black = (0,0,0)
    screen.blit(redSquare, (x, y))
    pygame.display.flip()



    choose = dm.dumbmenu(screen, ['Start Game',
                                        'Options',
                                        'Manual',
                                        'Show Highscore'], 200,150,None,35,1.4,black ,black)

    if choose == 0:
        Players()
        print ("You choose 'Start Game'.")
    elif choose == 1:
        opties()
        print ("You choose 'Options'.")
    elif choose == 2:
        story()
        print( "You choose 'Manual'.")
    elif choose == 3:
        Hoofdmenu()
        print ("You choose 'Show Highscore'.")
    elif choose == 4:
        print ("You choose 'Quit Game'.")




pygame.init()



def Players():
    redSquare = pygame.image.load('achtergrondopties.png').convert()
    white = (255,255,255)
    w = 700
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    black = (0,0,0)


    choose = dm.dumbmenu(screen,[
                            '- 3 spelers',
                            '- 4 spelers',
                            '- 5 spelers', '- 6 spelers',
                            '- speel met de computer',
                            '- terug naar het menu']
                            , 200,150,None,35,1.4,black ,black)


    if choose == 0:
        M.program()
        Hoofdmenu()
        print ("Je hebt gekozen voor 3 spelers.")
    elif choose == 1:
        Hoofdmenu()
        print ("Je hebt gekozen voor 4 spelers'.")
    elif choose == 2:
        Hoofdmenu()
        print( "Je hebt gekozen voor 5 spelers'.")
    elif choose == 3:
        Hoofdmenu()
        print ("Je hebt gekozen voor 6 spelers'.")
    elif choose == 4:
        Hoofdmenu()
        print ("Je hebt gekozen voor spelen met computer.")
    elif choose == 5:
        Hoofdmenu()
        print('Je hebt gekozen voor terug naar menu ')



def opties():

    redSquare = pygame.image.load('achtergrondSpelers.png').convert()
    white = (255,255,255)
    w = 700
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    black = (0,0,0)

    choose = dm.dumbmenu(screen,[
                            'Geluid uit',
                            'Taal wijzigen -> Engels',
                            'Terug naar het menu']
                            , 180,150,None,35,1.4,black ,black)


    if choose == 0:
        musicAan = False
        Hoofdmenu()
        print ("Je hebt gekozen voor Geluid uit'.")
    elif choose == 1:
        print ("Je hebt gekozen voor Taal wijzigen naar het engels''.")
    elif choose == 2:
        Hoofdmenu()
        print( "Je hebt gekozen voor Terug naar het menu'.")

def story():

    redSquare = pygame.image.load('Story.png').convert()
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
                    Hoofdmenu()
                    print('Einde terug naar menu')

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
#################################################################################################################################
#                                                                                                                               #
#
#################################################################################################################################

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
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels()






Hoofdmenu()
