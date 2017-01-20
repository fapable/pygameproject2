import uitproberen as F

import  Game as dm
import Opties as N
import spelers as S

pygame.init()


pygame.mixer.music.load("music.mp3")

red   = (255,  0,  0)
green =  ( 0,255,  0)
blue  =  ( 0,  0,255)
black = (0,0,0)
white = (255,255,255)
pygame.mixer.music.play(loops=0, start=0.0)
size = width, height = 340,240
screen = pygame.display.set_mode(size)
redSquare = pygame.image.load('background menu.png').convert()
white = (255,255,255)
w = 700
h = 420
screen = pygame.display.set_mode((w, h))
screen.fill((white))
x = 0
y = 0
screen.blit(redSquare, (x, y))
pygame.display.flip()



choose = dm.dumbmenu(screen, [
                                    'Start Game',
                                    'Options',
                                    'Manual',
                                    'Show Highscore',
                                    'Quit Game'], 200,150,None,45,1.4,black ,black)
def menu(choose):
    if choose == 0:
            S.Players()
            print ("You choose 'Start Game'.")
    elif choose == 1:
            N.opties()
            print ("You choose 'Options'.")
    elif choose == 2:
            F.story()
            print( "You choose 'Manual'.")
    elif choose == 3:
            print ("You choose 'Show Highscore'.")
    elif choose == 4:
            print ("You choose 'Quit Game'.")
menu(choose)





