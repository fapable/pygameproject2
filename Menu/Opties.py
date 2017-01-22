import pygame
import  Game as dm

def opties():

    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(loops=0, start=0.0)
    size = width, height = 340,240
    screen = pygame.display.set_mode(size)
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

    pygame.mixer.music.load("music.mp3")
    pygame.mixer.music.play(loops=0, start=0.0)
    choose = dm.dumbmenu(screen,[
                            'Geluid uit',
                            'Taal wijzigen -> Engels',
                            'Terug naar het menu']
                            , 180,150,None,35,1.4,black ,black)


    if choose == 0:
        print ("Je hebt gekozen voor Geluid uit'.")
    elif choose == 1:
        print ("Je hebt gekozen voor Taal wijzigen naar het engels''.")
    elif choose == 2:
        print( "Je hebt gekozen voor Terug naar het men'.")


