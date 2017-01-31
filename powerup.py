# foto powerup
pw1 = pygame.image.load('pw1.png')
pw2 = pygame.image.load('pw2.png')
pw3 = pygame.image.load('pw3.png')
pw4 = pygame.image.load('pw4.png')
pw5 = pygame.image.load('pw5.png')
pw6 = pygame.image.load('pw6.png')
pw7 = pygame.image.load('pw7.png')
pw8 = pygame.image.load('pw8.png')
pw9 = pygame.image.load('pw9.png')
pw10 = pygame.image.load('pw10.png')
helepowerup = [(1,16),(3,10),(6,17),(8,31),(10,22),(11,10),(13,27),(18,17),(19,9)]





# power up def
def powerupvak(self):
        global helepowerup
        if self.powerup == '':
            for i in helepowerup:
                if (self.pos.y,self.pos.x) == i and self.moves >= 0 and self.turn and self.alive and beurt == self.name:
                    if i == (1,16):
                        self.powerup = 'sniper'
                    elif i == (3,10):
                        self.powerup = 'wildfire'
                        screen.blit(pw9,(150,200))
                        pygame.display.flip()
                        time.sleep(8)
                        self.moves += 5
                        print("ja")
                    elif i == (6,17):
                        self.powerup = 'ufo'
                        screen.blit(pw4,(150,200))
                        pygame.display.flip()
                        time.sleep(8)
                        self.turn = False
                    elif i == (8,31):
                        self.powerup = 'plusultra'
                        screen.blit(pw6,(150,200))
                        pygame.display.flip()
                        time.sleep(8)
                        self.turn = False
                        print("ja")
                # upload image pw6
                    elif i == (10,22):
                        self.powerup = 'taxi'
                        screen.blit(pw2,(150,200))
                        pygame.display.flip()
                        time.sleep(8)
                        self.moves += 5
                        print("ja")
                    elif i == (11,10):
                        self.powerup = 'fiets'
                        screen.blit(pw1,(150,200))
                        pygame.display.flip()
                        time.sleep(8)
                        self.turn = False
                        print("ja")
                    elif i == (13,27):
                        self.powerup = 'slowdown'
                        screen.blit(pw7,(150,200))
                        pygame.display.flip()
                        time.sleep(8)
                        self.moves += 5
                        print("ja")
                    elif i == (18,17):
                        self.powerup = 'camouflage'
                        screen.blit(pw5,(150,200))
                        pygame.display.flip()
                        time.sleep(8)
                        self.moves += 5
                        print("ja")
                    elif i == (19,9):
                        self.powerup = 'fusrodah'
                        screen.blit(pw8,(150,200))
                        pygame.display.flip()
                        time.sleep(8)
                        self.turn = False
                        
                        
      # roepen in program
        p1.powerupvak()
        p2.powerupvak()
        p3.powerupvak()
        p4.powerupvak()
        p5.powerupvak()
        p6.powerupvak()
        
        
     ##################################################################
     #1e try
     
     def power(self):
        global fusro
        global fietss
        global wild
        global cam
        global tax
        global klok
        global box
        while True:
            if (self.pos.y, self.pos.x) == fusro  and self.moves >= 0 and self.turn and self.alive:
                screen.blit(pw8,(150,200))
                pygame.display.flip()
                time.sleep(8)
                self.turn = False
                print("ja")
                # upload image pw8
            elif (self.pos.y, self.pos.x) == fietss and self.moves >= 0 and self.turn and self.alive:
                screen.blit(pw1,(150,200))
                pygame.display.flip()
                time.sleep(8)
                self.turn = False
                print("ja")
                # upload image pw1
            elif (self.pos.y, self.pos.x) == wild and self.moves >= 0 and self.turn and self.alive:
                screen.blit(pw9,(150,200))
                pygame.display.flip()
                time.sleep(8)
                self.moves += 5
                print("ja")
                # upload image pw9
            elif (self.pos.y, self.pos.x) == cam and self.moves >= 0 and self.turn and self.alive:
                screen.blit(pw5,(150,200))
                pygame.display.flip()
                time.sleep(8)
                self.moves += 5
                print("ja")
                # upload image pw5
            elif (self.pos.y, self.pos.x) == tax and self.moves >= 0 and self.turn and self.alive:
                screen.blit(pw2,(150,200))
                pygame.display.flip()
                time.sleep(8)
                self.moves += 5
                print("ja")
                # upload image pw2
            elif (self.pos.y, self.pos.x) == klok and self.moves >= 0 and self.turn and self.alive:
                screen.blit(pw7,(150,200))
                pygame.display.flip()
                time.sleep(8)
                self.moves += 5
                print("ja")
                # upload image pw7
            elif (self.pos.y, self.pos.x) == box and self.moves >= 0 and self.turn and self.alive:
                screen.blit(pw6,(150,200))
                pygame.display.flip()
                time.sleep(8)
                self.turn = False
                print("ja")
                # upload image pw6
