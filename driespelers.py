import math
import pygame
import random
import input as N
import high_score as H

width = 1600
height = 1000
size = (width, height)
screen = pygame.display.set_mode(size)
sp1 = pygame.image.load('suprisekaart1.png')
sp2 = pygame.image.load('suprisekaart2.png')
sp6 = pygame.image.load('suprisekaart6.png')
sp7 = pygame.image.load('suprisekaart7.png')
sp8 = pygame.image.load('suprisekaart8.png')
sp10 = pygame.image.load('suprisekaart10.png')
sp12 = pygame.image.load('surprisekaarten12.png')
sp16 = pygame.image.load('surprisekaarten16.png')
sp27 = pygame.image.load('surprisekaarten27.png')
sp32 = pygame.image.load('surprisekaarten32.png')

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
boat = pygame.image.load('Boat.png')
hilton = pygame.image.load('hilton.png')
luxor = pygame.image.load('luxor.png')
abnamro = pygame.image.load('abnamro.png')
hro = pygame.image.load('hro.png')
kunsthal = pygame.image.load('kunsthal.png')
inntelhotels = pygame.image.load('inntelhotels.png')
woktogo = pygame.image.load('woktogo.png')
debijenkorf = pygame.image.load('debijenkorf.png')
huizejansen = pygame.image.load('huizejansen.png')
kabouterbuttplug = pygame.image.load('kabouterbuttplug.png')
kfcb = pygame.image.load('kfcb.png')
kfc = pygame.image.load('kfc.png')
oriental = pygame.image.load('oriental.png')
euromast = pygame.image.load('euromast.png')
coffeeshop = pygame.image.load('coffeeshopamigo.png')
dedoelen = pygame.image.load('dedoelen.png')
museumpark = pygame.image.load('museumpark.png')
erasmusmc = pygame.image.load('erasmusmc.png')
police = pygame.image.load('police.png')
endbutton = pygame.image.load('endturn.png')


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
helepolitie = [(0,16),(1,16),(2,16),(3,16),(6,16),(7,16),(8,16),(9,16),(10,16),(11,16),(12,16),(13,16),(16,16),(19,16)]
helelandmark = [(0,4),(0,21),(2,8),(3,14),(3,31),(4,19),(4,25),(8,11),(8,26),(11,19),(11,29),(14,12),(15,23),(16,29),(17,7),(19,14),(19,27),(11,16)]
startvakjes = [(7,0),(8,0),(9,0),(10,0),(11,0),(12,0)]
eindvakje = [(16,30)]


pl1 = 'player1'
pl2 = 'player2'
pl3 = 'player3'

beurt = pl1
lijn = -3
pos = ''


width = 1700
height = 1000
size = (width, height)
screen = pygame.display.set_mode(size)
droll = 1

abn = (3,14)
amazingoriental = (16,29)
bijenkorf = (8,11)
koffieshop = (19,14)
doelen = (17,7)
erasmus = (19,27)
euromast1 = (11,29)
hilton1 = (0,4)
hro1 = (0,21)
intellhotel =(4,25)
janzen = (11,16)
kabouter =(11,19)
kfc1 = (14,12)
kfc2 = (15,23)
kunsthal1 =(3,31)
luxor1 =(2,8)
museumpark1 =(8,26)
woktogo1 =(4,19)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

politielijn = False
politielijnmove1 = ""

def politielijnmove(screen):
    global lijn
    if politielijn:
        for row in range(0,20):
                for column in range(0,lijn+1):
                        if column <= 31:
                            screen.blit(police,(48 * column + 5,48 * row + 5))




def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

class Player:
    def __init__(self, name, namet,  x, y, image, objective1, objective2, objective3):
        self.name = name
        self.namet = namet
        self.pos = Vector(x, y)
        self.image = image
        self.moves = 0
        self.turn = True
        self.alive = True
        self.skip = False
        self.objective1 = objective1
        self.objective2 = objective2
        self.objective3 = objective3
        self.fichex = 0
        self.fichey = 0
        self.score = 0

    def dobbelsteen(self):
        uitkomst = random.randrange(1, 7)

        if uitkomst == 1:
            print("gegooide cijfer is 1")
            self.moves += 1
        elif uitkomst == 2:
            print("gegooide cijfer is 2")
            self.moves += 2
        elif uitkomst == 3:
            print("gegooide cijfer is 3")
            self.moves += 3
        elif uitkomst == 4:
            print("gegooide cijfer is 4")
            self.moves += 4
        elif uitkomst == 5:
            print("gegooide cijfer is 5")
            self.moves += 5
        elif uitkomst == 6:
            print("gegooide cijfer is 6")
            self.moves += 6


    def update(self):
        global beurt
        global pos
        if beurt == self.name:
            if self.moves >= 4 and (self.pos.y, self.pos.x) in startvakjes:
                keys = pygame.key.get_pressed()
                if keys[pygame.K_RIGHT]:
                    self.pos.y = 10
                    self.pos.x = 2
                    self.moves -= 1

            elif self.moves >= 4 and (self.pos.y, self.pos.x) in eindvakje:
                if self.objective1 == 'behaald' and self.objective2 == 'behaald' or self.objective1 == 'behaald' and self.objective3 == 'behaald' or self.objective2 == 'behaald' and self.objective3 == 'behaald':
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_DOWN]:
                        self.pos.y += 1
                        self.moves -= 1

            elif self.moves > 0 and self.alive:
                if self.skip:
                    print()
                    self.moves = 0
                    self.skip = False
                elif (self.pos.y, self.pos.x) in omhoog and (self.pos.y, self.pos.x) in omlaag and (self.pos.y, self.pos.x) in rechts :
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_UP]:
                        self.pos.y -= 1
                        self.moves -= 1
                    elif keys[pygame.K_DOWN]:
                        self.pos.y += 1
                        self.moves -= 1
                    elif keys[pygame.K_RIGHT]:
                        self.pos.x += 1
                        self.moves -= 1

                elif (self.pos.y, self.pos.x) in omhoog and (self.pos.y, self.pos.x) in omlaag:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_UP]:
                        self.pos.y -= 1
                        self.moves -= 1
                    elif keys[pygame.K_DOWN]:
                        self.pos.y += 1
                        self.moves -= 1

                elif (self.pos.y, self.pos.x) in rechts and (self.pos.y, self.pos.x) in omlaag:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_RIGHT]:
                        self.pos.x += 1
                        self.moves -= 1
                    elif keys[pygame.K_DOWN]:
                        self.pos.y += 1
                        self.moves -= 1

                elif (self.pos.y, self.pos.x) in rechts and (self.pos.y, self.pos.x) in omhoog:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_RIGHT]:
                        self.pos.x += 1
                        self.moves -= 1
                    elif keys[pygame.K_UP]:
                        self.pos.y -= 1
                        self.moves -= 1

                elif (self.pos.y, self.pos.x) in rechts:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_RIGHT]:
                        self.pos.x += 1
                        self.moves -= 1

                elif (self.pos.y, self.pos.x) in omhoog:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_UP]:
                        self.pos.y -= 1
                        self.moves -= 1

                elif (self.pos.y, self.pos.x) in omlaag:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_DOWN]:
                        self.pos.y += 1
                        self.moves -= 1

                elif (self.pos.y, self.pos.x) in links:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_LEFT]:
                        self.pos.x -= 1
                        self.moves -= 1

                elif (self.pos.y, self.pos.x) in startvakjes:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_RIGHT]:
                        self.moves = 0

                elif (self.pos.y, self.pos.x) in eindvakje:
                    keys = pygame.key.get_pressed()
                    if keys[pygame.K_DOWN]:
                        self.moves = 0

            elif self.moves == 0 and beurt == pl1 and self.turn == True:
                beurt = pl2
                self.turn = False
            elif self.moves == 0 and beurt == pl2 and self.turn == True:
                beurt = pl3
                self.turn = False
            elif self.moves == 0 and beurt == pl3 and self.turn == True:
                beurt = pl1
                self.turn = False

            elif not self.alive and self.moves > 0 and self.turn == True:
                self.moves = 0

    def turns(self):
        if not(self.turn) and beurt == self.name and self.moves == 0:
            self.turn = True
            Player.dobbelsteen(self)


    def draw(self, screen):
        screen.blit(self.image, (48 * self.pos.x + 5, 48 * self.pos.y + 5, 43, 43))


    def police(self):
        global politielijn
        global politielijnmove1
        for p in helepolitie:
            if (self.pos.y,self.pos.x) == (p) and not politielijn:
                politielijn = True
                politielijnmove1 = self.name
                pygame.mixer.music.load("siren.mp3")
                pygame.mixer.music.play(loops=0, start=0.6)


    def check(self):
        global lijn
        global politielijnmove1
        if politielijn and self.name == politielijnmove1 and self.moves == 0 and self.turn:
            lijn += 2
        elif self.pos.x <= lijn:
            self.alive = False
    def chance(self):
        global chance_vakjes
        for i in chance_vakjes:
            if (self.pos.y, self.pos.x) == i and self.moves == 0 and self.turn and self.alive:
                    supr = random.randrange(1,3)
                    if supr == 1:
                        self.skip = True
                        print("beurt over slaan")
                        # upload image sp1
                    elif supr == 2:
                        self.moves += 5
                        print("5stappen")
                        # upload image sp6
    def movesleft(self):
        if self.name == beurt and self.turn and self.alive:
            largeText = pygame.font.Font('freesansbold.ttf',23)
            TextSurf, TextRect = text_objects('moves left ' + str(self.moves), largeText)
            TextRect.center = ((1615),(170))
            screen.blit(TextSurf, TextRect)
            screen.blit(pygame.transform.scale(self.image,(135,135)), (1550, 1))
            screen.blit(endbutton, (1550, 865, 43, 43))
    def landmark(self):
        if (self.pos.y,self.pos.x) == self.objective1:
            self.objective1 = 'behaald'
            print('OBJECTIVE BEHAALD')
        elif (self.pos.y,self.pos.x) == self.objective2:
            self.objective2 = 'behaald'
            print('OBJECTIVE BEHAALD')
        elif (self.pos.y,self.pos.x) == self.objective3:
            self.objective3 = 'behaald'
            print('OBJECTIVE BEHAALD')
    def fichedev(self):
        global helelandmark
        for i in helelandmark:
            if (self.pos.y,self.pos.x) == i:
                self.fichex = i[0]
                self.fichey = i[1]
    def winner(self):
        if (self.pos.x, self.pos.y) == (2, 0) and self.moves == 0 and self.turn and self.alive:
            # upload winner screen
            H.insert_naam(self.namet, self.score)
            H.update_score(self.namet, self.score)



Margin = 5
# Handle pygame events
def process_events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # Give the signal to quit
            return True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            return False
    return False




def rollobjective1():
    resultobjective1 = random.randrange(1, 19)

    if resultobjective1 == 1:
        return abn
    elif resultobjective1 == 2:
        return amazingoriental
    elif resultobjective1 == 3:
        return bijenkorf
    elif resultobjective1 == 4:
        return koffieshop
    elif resultobjective1 == 5:
        return doelen
    elif resultobjective1 == 6:
        return erasmus
    elif resultobjective1 == 7:
        return euromast1
    elif resultobjective1 == 8:
        return hilton1
    elif resultobjective1 == 9:
        return hro1
    elif resultobjective1 == 10:
        return intellhotel
    elif resultobjective1 == 11:
        return janzen
    elif resultobjective1 == 12:
        return kabouter
    elif resultobjective1 == 13:
        return kfc1
    elif resultobjective1 == 14:
        return kfc2
    elif resultobjective1 == 15:
        return kunsthal1
    elif resultobjective1 == 16:
        return luxor1
    elif resultobjective1 == 17:
        return museumpark1
    elif resultobjective1 == 18:
        return woktogo1
def rollobjective2():
    resultobjective1 = random.randrange(1, 19)

    if resultobjective1 == 1:
        return abn
    elif resultobjective1 == 2:
        return amazingoriental
    elif resultobjective1 == 3:
        return bijenkorf
    elif resultobjective1 == 4:
        return koffieshop
    elif resultobjective1 == 5:
        return doelen
    elif resultobjective1 == 6:
        return erasmus
    elif resultobjective1 == 7:
        return euromast1
    elif resultobjective1 == 8:
        return hilton1
    elif resultobjective1 == 9:
        return hro1
    elif resultobjective1 == 10:
        return intellhotel
    elif resultobjective1 == 11:
        return janzen
    elif resultobjective1 == 12:
        return kabouter
    elif resultobjective1 == 13:
        return kfc1
    elif resultobjective1 == 14:
        return kfc2
    elif resultobjective1 == 15:
        return kunsthal1
    elif resultobjective1 == 16:
        return luxor1
    elif resultobjective1 == 17:
        return museumpark1
    elif resultobjective1 == 18:
        return woktogo1
def rollobjective3():
    resultobjective1 = random.randrange(1, 19)

    if resultobjective1 == 1:
        return abn
    elif resultobjective1 == 2:
        return amazingoriental
    elif resultobjective1 == 3:
        return bijenkorf
    elif resultobjective1 == 4:
        return koffieshop
    elif resultobjective1 == 5:
        return doelen
    elif resultobjective1 == 6:
        return erasmus
    elif resultobjective1 == 7:
        return euromast1
    elif resultobjective1 == 8:
        return hilton1
    elif resultobjective1 == 9:
        return hro1
    elif resultobjective1 == 10:
        return intellhotel
    elif resultobjective1 == 11:
        return janzen
    elif resultobjective1 == 12:
        return kabouter
    elif resultobjective1 == 13:
        return kfc1
    elif resultobjective1 == 14:
        return kfc2
    elif resultobjective1 == 15:
        return kunsthal1
    elif resultobjective1 == 16:
        return luxor1
    elif resultobjective1 == 17:
        return museumpark1
    elif resultobjective1 == 18:
        return woktogo1

# Main program logic
def program():


    # Start PyGame
    pygame.init()

    # Set the resolution


    # Set up the default font
    font = pygame.font.Font(None, 30)
    pygame.display.set_caption("Ontsnapperdam")

    p1 = Player("player1", N.name(), 0, 7, rund, rollobjective1(), rollobjective2(), rollobjective3())
    p2 = Player("player2", N.name(), 0, 8, kim, rollobjective1(), rollobjective2(), rollobjective3())
    p3 = Player("player3", N.name(),0, 9, trump, rollobjective1(), rollobjective2(), rollobjective3())


    while not process_events():
        p1.update()
        p2.update()
        p3.update()

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
                elif row == 17 and column == 28:
                    screen.blit(boat,(48 * column + 5,48 * row + 5))
                elif row == 16 and column == 5:
                    screen.blit(dedoelen,(48 * column + 5, 48 * row + 5))
                elif row == 17 and column == 14:
                    screen.blit(coffeeshop,(48 * column + 5, 48 * row + 5))
                elif row == 17 and column == 24:
                    screen.blit(erasmusmc,(48 * column + 5, 48 * row + 5))
                elif row == 1 and column == 3:
                    screen.blit(hilton,(48 * column + 5, 48 * row + 5))
                elif row == 8 and column == 28:
                    screen.blit(euromast,(48 * column + 5, 48 * row + 5))
                elif row == 7 and column == 23:
                    screen.blit(museumpark,(48 * column + 5, 48 * row + 5))
                elif row == 14 and column == 28:
                    screen.blit(oriental,(48 * column + 5, 48 * row + 5))
                elif row == 8 and column == 28:
                    screen.blit(euromast,(48 * column + 5, 48 * row + 5))
                elif row == 14 and column == 10:
                    screen.blit(kfc,(48 * column + 5, 48 * row + 5))
                elif row == 8 and column == 28:
                    screen.blit(euromast,(48 * column + 5, 48 * row + 5))
                elif row == 3 and column == 8:
                    screen.blit(luxor,(48 * column + 5, 48 * row + 5))
                elif row == 1 and column == 13:
                    screen.blit(abnamro,(48 * column + 5, 48 * row + 5))
                elif row == 9 and column == 10:
                    screen.blit(debijenkorf,(48 * column + 5, 48 * row + 5))
                elif row == 4 and column == 17:
                    screen.blit(woktogo,(48 * column + 5, 48 * row + 5))
                elif row == 10 and column == 14:
                    screen.blit(huizejansen,(48 * column + 5, 48 * row + 5))
                elif row == 14 and column == 21:
                    screen.blit(kfcb,(48 * column + 5, 48 * row + 5))
                elif row == 10 and column == 17:
                    screen.blit(kabouterbuttplug,(48 * column + 5, 48 * row + 5))
                elif row == 1 and column == 20:
                    screen.blit(hro,(48 * column + 5, 48 * row + 5))
                elif row == 2 and column == 24:
                    screen.blit(inntelhotels,(48 * column + 5, 48 * row + 5))
                elif row ==2 and column == 29:
                    screen.blit(kunsthal,(48 * column + 5, 48 * row + 5))


        p1.draw(screen)
        p2.draw(screen)
        p3.draw(screen)

        p1.turns()
        p2.turns()
        p3.turns()
        p1.police()
        p2.police()
        p3.police()

        p1.check()
        p2.check()
        p3.check()

        p1.movesleft()
        p2.movesleft()
        p3.movesleft()

        politielijnmove(screen)
        p1.landmark()
        p2.landmark()
        p3.landmark()

        p1.fichedev()
        p2.fichedev()
        p3.fichedev()

        p1.chance()
        p2.chance()
        p3.chance()

        p1.winner()
        p2.winner()
        p3.winner()



        # Draw the score text
        #score_text = font.render("Score: 100", 1, (255, 0, 0))
        #8screen.blit(score_text, (16, 16))
        # Flip the screen
        clock = pygame.time.Clock()
        clock.tick(60)
        pygame.display.flip()
