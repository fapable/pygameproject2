def chance(self):
        global chance_vakjes
        for i in chance_vakjes:
            if (self.pos.y, self.pos.x) == i and self.moves == 0 and self.turn and self.alive:
                    supr = random.randrange(1,12)
                    if supr == 1:
                        if self.verder :
                            self.skip = False
                            self.verder = False
                            screen.blit(sp1,(150,200))
                            pygame.display.flip()
                            time.sleep(0)
                            print("ga verder")

                        else:
                            self.skip = True
                            self.verder = True
                            screen.blit(sp1, (150,200))
                            pygame.display.flip()
                            time.sleep(0)
                            print("beurt wachten")
                        # upload image sp1
                    elif supr == 2:
                        if self.verder :
                            self.skip = False
                            self.verder = False
                            screen.blit(sp2,(150,200))
                            pygame.display.flip()
                            time.sleep(0)
                            print("ga verder")

                        else:
                            self.skip = True
                            self.verder = True
                            screen.blit(sp2, (150,200))
                            pygame.display.flip()
                            time.sleep(1)
                            print("beurt wachten")

                         # upload image sp2
                    elif supr == 3:
                        screen.blit(sp25, (150,200))
                        pygame.display.flip()
                        time.sleep(8)
                        self.moves += 5
                        print("5stappen")
                        # upload image sp25
                    elif supr == 4:
                        if self.verder :
                            self.skip = False
                            self.verder = False
                            screen.blit(sp13,(150,200))
                            pygame.display.flip()
                            time.sleep(0)
                            print("ga verder")

                        else:
                            self.skip = True
                            self.verder = True
                            screen.blit(sp3, (150,200))
                            pygame.display.flip()
                            time.sleep(1)
                            print("beurt wachten")
                    elif supr == 5:

                        screen.blit(sp18, (150,200))
                        pygame.display.flip()
                        time.sleep(8)
                        self.moves += 1
                        # upload image sp7
                    elif supr == 6:
                        self.turn = False
                        screen.blit(sp20, (150,200))
                        pygame.display.flip()
                        time.sleep(8)
                        print("gooi nog een keer")
                        # gooi nog een keer
                        # upload image sp20
                    elif supr == 7:
                        self.turn = False
                        screen.blit(sp12, (150,200))
                        pygame.display.flip()
                        time.sleep(8)
                        print("gooi nog een keer")
                        # gooi nog een keer
                        # upload image sp12
                    elif supr == 8:
                        screen.blit(sp16, (150,200))
                        pygame.display.flip()
                        time.sleep(8)
                        pass
                        # gebeurt niks
                        # upload image sp16
                    elif supr == 9:
                        screen.blit(sp19, (150,200))
                        pygame.display.flip()
                        time.sleep(8)
                        self.moves += 1
                        print("dobbel  + 1")
                        # next worp + 1
                        # upload image sp18
                    elif supr == 10:
                        screen.blit(sp32, (150,200))
                        pygame.display.flip()
                        time.sleep(8)
                        pass
                        # niks
                        # upload image sp32
                    elif supr == 11:
                        self.dobbel = True
                        screen.blit(sp19, (150,200))
                        pygame.display.flip()
                        time.sleep(8)
                        self.moves += 1
                        print("dobbel  + 1")
                        # next worp + 1
                        # upload image sp19
                        
                ####################################
                # vergeet niet om hem aanteroepen   #
                #######################################
