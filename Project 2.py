import math
import pygame
import random

attack = pygame.image.load('Attack.png')
chance = pygame.image.load('Chance1.png')
normale = pygame.image.load('Normale.png')
politie = pygame.image.load('Politielijn.png')
politiec = pygame.image.load('PolitielijnChance.png')
landmark = pygame.image.load('Powerup.png')
badge = pygame.image.load('Badge.png')
chanceattack = pygame.image.load('ChanceAttack.png')
politielijnmark = pygame.image.load('PolitielijnPowerup.png')
politielijnattack = pygame.image.load('PolitielijnAttack.png')
politielijnbadge = pygame.image.load('Politielijnbadge.png')
plusultra = pygame.image.load('Plusultra.png')
fusrodah = pygame.image.load('Fusrodah.png')
slowdowntime = pygame.image.load('Slowdowntime.png')
taxi = pygame.image.load('Taxi.png')
ufo = pygame.image.load('Ufo.png')
wildfire = pygame.image.load('Wildfire.png')
fiets = pygame.image.load('Fiets.png')
camo = pygame.image.load('Camo.png')
end = pygame.image.load('End.png')
begin1 = pygame.image.load('begin1.png')
begin2 = pygame.image.load('begin2.png')
begin3 = pygame.image.load('begin3.png')
sniper = pygame.image.load('Sniper.png')
dice_one = pygame.image.load("dice_one.png")
dice_two = pygame.image.load("dice_two.png")
dice_three = pygame.image.load("dice_three.png")
dice_four = pygame.image.load("dice_four.png")
dice_five = pygame.image.load("dice_five.png")
dice_six = pygame.image.load("dice_six.png")
obama = pygame.image.load("obamaspeler.png")
kim = pygame.image.load("kimkspeler.png")
trump = pygame.image.load("trumpspeler.png")
rund = pygame.image.load("rundfunkspeler.png")
snoopdog = pygame.image.load("snoopdogspeler.png")
gw = pygame.image.load("geertwildersspeler.png")
black = 0, 0, 0
white = 255, 255, 255
red = 255, 0, 0
green = 0, 255, 0
blue = 0, 0, 255

normale_vakjes = [(3,15),(0,2),(0,3),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,10),(0,11),(0,13),(0,14),(0,17),(0,18),(0,19),(0,20),(0,22),(0,23),(0,24),(0,25),(0,27),(0,28),(0,29),(0,30),(0,31),(1,2),(1,8),(1,12),(2,2)
,(2,12),(2,31),(3,2,),(3,12),(3,13),(3,18),(3,19),(4,2),(4,14),(4,24),(4,26),(4,27),(4,31),(5,12),(5,24),(5,26),(5,28),(5,31),(19,2),(19,3),(19,4),(19,10),(19,11),(19,12),(19,13),(19,15),(19,17),(19,18),(19,19),(19,21),(19,22),(19,23),(19,24),(19,25),(19,26),(18,2),(18,27),(17,2),(17,8),(17,17),(17,21),(17,22),(17,23),(17,27),(16,9),(16,17),(16,18),(16,19),(16,20),(16,23),(15,2),(15,7),(15,8),(15,9),(15,11),(15,12),(15,20),(15,31),(14,2),(14,7),(14,20),(14,23),(14,31),(13,2),(13,13),(13,14),(13,17),(13,19),(13,20),(13,24),(13,25),(13,26),(13,31),(12,2),(12,7),(12,19),(12,26),(12,31),(11,7),(11,8),(11,9),(11,27),(11,28),(11,30),(11,31),(10,3),(10,4),(10,7),(10,20),(10,21),(10,26),(10,31),(9,5),(9,6),(9,7),(9,22),(9,26),(8,7),(8,10),(8,12),(7,2),(7,10),(7,13),(7,22),(7,26),(6,2),(6,8),(6,12),(6,13),(6,20),(6,21),(6,22),(6,24)]
chanceattack_vakjes = [(2,10),(6,10),(6,19),(16,15),(16,27),(19,7)]
badge_vakjes = [(4,28),(6,7),(10,19),(15,10),(17,20)]
landmark_vakjes = [(0,4),(0,21),(2,8),(3,14),(3,31),(4,19),(4,25),(8,11),(8,26),(11,19),(11,29),(14,12),(15,23),(16,29),(17,7),(19,14),(19,27)]
politie_vakjes = [(2,16),(3,16),(7,16),(9,16),(10,16),(12,16),(19,16)]
attack_vakjes = [(2,9),(4,10),(5,10),(5,14),(5,19),(6,9),(6,14),(6,15),(6,18),(6,28),(6,29),(6,30),(6,31),(7,31),(11,11),(11,12),(12,12),(13,15),(14,15),(14,27),(15,15),(15,27),(16,28),(18,7),(19,5),(19,6),(19,8)]
chance_vakjes = [(0,12),(0,15),(0,26),(1,31),(3,17),(4,12),(5,2),(6,23),(6,26),(7,7),(8,13),(8,22),(9,4),(9,31),(11,26),(13,7),(13,12),(13,18),(13,23),(16,2),(16,31),(17,9),(19,20)]
rechts = [(19,2),(10,19),(13,15),(11,8),(11,11),(15,10),(6,7),(19,26),(19,9),(17,20),(11,29),(0,16),(3,16),(6,16),(13,16),(16,16),(19,16),(2,9),(6,9),(11,9),(11,10),(19,5),(19,6),(19,7),(19,8),(14,15),(14,16),(16,15),(16,16),(6,14),(6,15),(6,17),(6,18),(6,19),(6,28),(6,29),(6,30),(16,27),(16,28),(0,12),(0,15),(0,26),(3,17),(6,19),(6,23),(9,4),(11,26),(13,12),(13,18),(13,23),(16,15),(16,26),(19,7),(19,20),(0,2),(0,3),(0,5),(0,6),(0,7),(0,8),(0,9),(0,10),(0,11),(0,13),(0,14),(0,17),(0,18),(0,19),(0,20),(0,22),(0,23),(0,24),(0,25),(0,27),(0,28),(0,29),(0,30),(3,12),(3,13),(3,15),(3,18),(4,24),(4,26),(4,27),(6,8),(6,12),(6,13),(6,20),(6,21),(6,22),(8,10),(8,12),(9,5),(9,6),(10,2),(10,3),(10,20),(10,21),(11,7),(11,9),(11,9),(11,27),(11,28),(11,30),(13,13),(13,14),(13,17),(13,19),(13,24),(13,25),(13,26),(15,7),(15,8),(15,9),(15,11),(16,17),(16,18),(16,19),(17,8),(17,21),(17,22),(19,2),(19,3),(19,4),(19,10),(19,11),(19,12),(19,13),(19,15),(19,17),(19,18),(19,19),(19,21),(19,22),(19,23),(19,24),(19,25),(6,19),(16,15),(16,27),(19,7),(0,4),(0,21),(2,8),(3,14),(4,25),(8,11),(11,28),(19,14),(16,29),(17,7)]
omhoog = [(7,13),(18,17),(10,22),(7,16),(11,19),(13,16),(13,19),(19,27),(1, 2),(2,16),(1,16),(13,16),(12,16),(11,16),(10,16),(9,16),(8,16),(7,17),(19,7),(18,7),(6,14),(5,14),(5,2),(17,9),(13,7),(7,7),(8,13),(4,12),(8,22),(11,16),(18,2),(17,2),(15,2),(14,2),(13,2),(12,2),(11,2),(10,2),(9,2),(8,2),(7,2),(6,2),(4,2),(3,2),(2,2),(1,1),(10,4),(9,7),(8,7),(16,9),(15,12),(4,14),(19,17),(17,17),(12,19),(9,22),(7,22),(17,23),(16,23),(14,23),(6,24),(5,24),(13,26),(12,26),(10,26),(9,26),(7,26),(5,26),(18,27),(17,27),(14,12),(15,23),(8,26)]
omlaag = [(5,28),(14,7),(7,16),(8,16),(9,16),(10,16),(11,16),(12,16),(6,16),(0,16),(1,16),(2,16),(2,10),(3,10),(4,10),(5,10),(6,10),(11,12),(12,12),(5,14),(13,15),(14,15),(15,15),(5,19),(13,27),(14,27),(15,27),(6,31),(7,31),(8,31),(16,2),(13,7),(0,12),(4,12),(6,26),(1,31),(9,31),(18,2),(17,2),(15,2),(14,2),(13,2),(12,2),(11,2),(10,2),(9,2),(8,2),(8,7),(9,7),(10,7),(11,7),(12,7),(0,8),(1,8),(7,10),(1,12),(2,12),(3,12),(5,12),(4,14),(16,17),(17,17),(3,19),(14,20),(13,20),(15,20),(16,20),(4,26),(5,26),(7,26),(9,26),(10,26),(12,26),(0,31),(2,31),(4,31),(5,31),(10,31),(11,31),(12,31),(13,31),(14,31),(15,31),(2,10),(6,10),(4,28),(3,14),(4,19),(8,26),(3,31)]
links = [(16,31)]




width = 1700
height = 1000
size = (width, height)
screen = pygame.display.set_mode(size)
droll = 1

class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Player:
    def __init__(self, name, x, y, image):
        self.name = name
        self.pos = Vector(x, y)
        self.image = image


    def update(self):
        if (self.pos.y, self.pos.x) in omhoog and (self.pos.y, self.pos.x) in omlaag and (self.pos.y, self.pos.x) in rechts :
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.pos.y -= 1
            elif keys[pygame.K_DOWN]:
                self.pos.y += 1
            elif keys[pygame.K_RIGHT]:
                self.pos.x += 1

        elif (self.pos.y, self.pos.x) in omhoog and (self.pos.y, self.pos.x) in omlaag:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.pos.y -= 1
            elif keys[pygame.K_DOWN]:
                self.pos.y += 1

        elif (self.pos.y, self.pos.x) in rechts and (self.pos.y, self.pos.x) in omlaag:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.pos.x += 1
            elif keys[pygame.K_DOWN]:
                self.pos.y += 1

        elif (self.pos.y, self.pos.x) in rechts and (self.pos.y, self.pos.x) in omhoog:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.pos.x += 1
            elif keys[pygame.K_UP]:
                self.pos.y -= 1

        elif (self.pos.y, self.pos.x) in rechts:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_RIGHT]:
                self.pos.x += 1

        elif (self.pos.y, self.pos.x) in omhoog:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_UP]:
                self.pos.y -= 1

        elif (self.pos.y, self.pos.x) in omlaag:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_DOWN]:
                self.pos.y += 1

        elif (self.pos.y, self.pos.x) in links:
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]:
                self.pos.x -= 1


    def draw(self, screen):
        screen.blit(self.image, (48 * self.pos.x + 5, 48 * self.pos.y + 5, 43, 43))








'''class Enemy:
    def __init__(self, x, y, r):
        self.x = x
        self.y = y
        self.r = r
        self.health = 255

    def update(self, player):
        # If this enemy is colliding with the player
        if math.sqrt((player.x - self.x) ** 2 +
                     (player.y - self.y) ** 2) < self.r + player.r:
            self.health -= 1
            if self.health == 0:
                self.health = 255

    def draw(self, screen):
        pygame.draw.circle(screen, (self.health, 0, 0),
                           (int(self.x), int(self.y)), int(self.r))'''

Margin = 5
# Handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True

    return False

'''class Vakjes:
    def __init__(self,position,row,column):
        self.Pos = position
        self.x = row
        self.y = column

    def draw(self,screen):
        pygame.draw.rect(screen, (255,255,255), (self.x,self.y,50,50), 0)'''

# Main program logic
def program():


    # Start PyGame
    pygame.init()

    # Set the resolution


    # Set up the default font
    font = pygame.font.Font(None, 30)
    pygame.display.set_caption("Ontsnapperdam")

    Player1 = Player("player1",2,8, rund)
    Player2 = Player("player2",2,9, kim)
    Player3 = Player("player3",2,10, trump)

    while not process_events():
        Player.update(Player1)
        Player.update(Player2)
        Player.update(Player3)

        # Clear the screen
        screen.fill((255,255,255))

        #draw board
        for row in range(0,20):
            for column in range(0,32):
                for i in normale_vakjes:
                    if (row,column) == i :
                        #pygame.draw.rect(screen, (255,255,255), (48 * column + 5 ,48 * row + 5,43,43), 0)
                        screen.blit(normale,(48 * column + 5,48 * row + 5))
                    elif row == 7 and column == 0:
                        pygame.draw.rect(screen, (0,0,0), (48 * column + 5 ,48 * row + 5,43,43), 0)
                    elif row == 8 and column == 0:
                        pygame.draw.rect(screen, (255,0,0), (48 * column + 5 ,48 * row + 5,43,43), 0)
                    elif row == 9 and column == 0:
                        pygame.draw.rect(screen, (255,0,255), (48 * column + 5 ,48 * row + 5,43,43), 0)
                    elif row == 10 and column == 0:
                        pygame.draw.rect(screen, (0,255,255), (48 * column + 5 ,48 * row + 5,43,43), 0)
                    elif row == 11 and column == 0:
                        pygame.draw.rect(screen, (255,255,0), (48 * column + 5 ,48 * row + 5,43,43), 0)
                    elif row == 12 and column == 0:
                        pygame.draw.rect(screen, (0,255,0), (48 * column + 5 ,48 * row + 5,43,43), 0)
                    elif row == 9 and column == 1:
                        pygame.draw.rect(screen, (255,255,255), (48 * column + 5 ,(48 * row + 5)+24,43,43), 0)
                        screen.blit(normale,(48 * column + 5,(48 * row + 5)+24))
                    elif row == 8 and column == 2:
                        pygame.draw.rect(screen, (255,255,255), ((48 * column + 5 ),48 * row + 5,43,187), 0)
                for a in attack_vakjes:
                    if (row,column) == a:
                        screen.blit(attack,(48 * column + 5,48 * row + 5))
                for c in chance_vakjes:
                    if (row,column) == c:
                        screen.blit(chance,(48 * column + 5,48 * row + 5))
                for ca in chanceattack_vakjes:
                    if (row,column) == ca:
                        screen.blit(chanceattack,(48 * column + 5,48 * row + 5))
                for p in politie_vakjes:
                    if (row,column) ==  p:
                        screen.blit(politie,(48 * column + 5,48 * row + 5))
                    elif row == 13 and column == 16 or row == 16 and column == 16 or row == 6 and column == 16:
                        screen.blit(politielijnattack,(48 * column + 5,48 * row + 5))
                    elif row == 8 and column == 16:
                        screen.blit(politiec,(48 * column + 5,48 * row + 5))
                    elif row == 11 and column == 16:
                        screen.blit(politielijnmark,(48 * column + 5,48 * row + 5))
                    elif row == 0 and column == 16:
                        screen.blit(politielijnbadge,(48 * column + 5,48 * row + 5))
                for u in landmark_vakjes:
                    if (row,column) == u:
                        screen.blit(landmark,(48 * column + 5,48 * row + 5))
                for b in badge_vakjes:
                    if (row,column) == b:
                        screen.blit(badge,(48 * column + 5,48 * row + 5))
                if row == 3 and column == 10:
                    screen.blit(wildfire,(48 * column + 5,48 * row + 5))
                elif row == 6 and column == 17:
                    screen.blit(ufo,(48 * column + 5,48 * row + 5))
                elif row == 8 and column == 31:
                    screen.blit(plusultra,(48 * column + 5,48 * row + 5))
                elif row == 10 and column == 22:
                    screen.blit(taxi,(48 * column + 5,48 * row + 5))
                elif row == 11 and column == 10:
                    screen.blit(fiets,(48 * column + 5,48 * row + 5))
                elif row == 13 and column == 27:
                    screen.blit(slowdowntime,(48 * column + 5,48 * row + 5))
                elif row == 18 and column == 17:
                    screen.blit(camo,(48 * column + 5,48 * row + 5))
                elif row == 19 and column == 9:
                    screen.blit(fusrodah,(48 * column + 5,48 * row + 5))
                elif row == 16 and column == 30:
                    screen.blit(end,(48 * column + 5,48 * row + 5))
                elif row == 8 and column == 2:
                    screen.blit(begin2,(48 * column + 5,48 * row + 5))
                elif row == 9 and column == 2 or row == 10 and column == 2:
                    screen.blit(begin1,(48 * column + 5,48 * row + 5))
                elif row == 11 and column == 2:
                    screen.blit(begin3,(48 * column + 5,48 * row + 5))
                elif row == 1 and column == 16:
                    screen.blit(sniper,(48 * column + 5,48 * row + 5))

        Player1.draw(screen)
        Player2.draw(screen)
        Player3.draw(screen)

            # Draw the score text
        #score_text = font.render("Score: 100", 1, (255, 0, 0))
        #8screen.blit(score_text, (16, 16))
        pygame.display.update()
        # Flip the screen
        clock = pygame.time.Clock()
        clock.tick(60)
        pygame.display.flip()

program()
