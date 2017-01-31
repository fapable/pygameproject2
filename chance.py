
# Foto's van de kaartjes
sp1 = pygame.image.load('suprisekaart1.png')
sp2 = pygame.image.load('suprisekaart2.png')
sp3 = pygame.image.load('suprisekaart3.png')
sp6 = pygame.image.load('suprisekaart6.png')
sp7 = pygame.image.load('suprisekaart7.png')
sp8 = pygame.image.load('suprisekaart8.png')
sp10 = pygame.image.load('suprisekaart10.png')
sp12 = pygame.image.load('surprisekaarten12.png')
sp16 = pygame.image.load('surprisekaarten16.png')
sp32 = pygame.image.load('surprisekaarten32.png')
spr4 = pygame.image.load('suprisekaart4.png')
spr31 = pygame.image.load('surprisekaarten31.png')
sp18 = pygame.image.load('surprisekaarten18.png')
sp19 = pygame.image.load('surprisekaarten19.png')
sp20 = pygame.image.load('surprisekaarten20.png')


# Methode moet in de class Player
def chance(self):
        global chance_vakjes
        for i in chance_vakjes:
            if (self.pos.y, self.pos.x) == i and self.moves == 0 and self.turn and self.alive:
                    supr = random.randrange(1,12) # niet alle kaartjen worden nu random gekozen
                    if supr == 1:
                        if self.moves == 0:
                            pass
                        else:
                            self.skip = True

                        # upload image sp1
                    elif supr == 2:
                        self.skip = True
                        print("beurt over slaan")

                         # upload image sp2
                    elif supr == 3:
                        self.moves += 5
                        print("5stappen")
                        # upload image sp6
                    elif supr == 4:
                        self.skip = True
                        print("beurt over slaan")
                         # upload image sp3
                    elif supr == 5:
                        self.moves += 1
                        # upload image sp7
                    elif supr == 6:
                        self.turn = False
                        print("gooi nog een keer")
                        # gooi nog een keer
                        # upload image sp20
                    elif supr == 7:
                        self.turn = False
                        print("gooi nog een keer")
                        # gooi nog een keer
                        # upload image sp12
                    elif supr == 8:
                        pass
                        # gebeurt niks
                        # upload image sp16
                    elif supr == 9:
                        self.dobbel = True
                        print("dobbel  + 1")
                        # next worp + 1
                        # upload image sp18
                    elif supr == 10:
                        pass
                        # niks
                        # upload image sp32
                    elif supr == 11:
                        self.dobbel = True
                        print("dobbel  + 1")
                        # next worp + 1
                        # upload image sp19
                    elif supr == 12:
                        pass
                        # Ga terug naar je meest recente landmark
                        # upload image sp10
                    elif supr == 13:
                        pass
                        # 1 van je Quest is volbracht
                        # upload image sp7
