import pygame
import  Game as dm
pygame.init()



def Players():
    pygame.mixer.music.load("music.mp3")

    pygame.mixer.music.play(loops=0, start=0.0)
    size = width, height = 340,240
    screen = pygame.display.set_mode(size)
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


    pygame.mixer.music.play(loops=0, start=0.0)
    choose = dm.dumbmenu(screen,[
                            '- 3 spelers',
                            '- 4 spelers',
                            '- 5 spelers', '- 6 spelers',
                            '- speel met de computer',
                            '- terug naar het menu']
                            , 200,150,None,35,1.4,black ,black)


    if choose == 0:
        print ("Je hebt gekozen voor 3 spelers.")
    elif choose == 1:
        print ("Je hebt gekozen voor 4 spelers'.")
    elif choose == 2:
        print( "Je hebt gekozen voor 5 spelers'.")
    elif choose == 3:
        print ("Je hebt gekozen voor 6 spelers'.")
    elif choose == 4:
        print ("Je hebt gekozen voor spelen met computer.")
    elif choose == 5:
        print('Je hebt gekozen voor terug naar menu ')


