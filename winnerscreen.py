# Moet in de player class aan het einde
def winnerscreen(self):
        global beurt

        if (self.pos.x,self.pos.y) == (16,30) and self.moves == 0 and self.turn and self.alive:
                foto(self.namet)



####
# deze moet boven de player class



def foto (name):
    redSquare = pygame.image.load('winnerscreen.png')
    white = (255,255,255)
    w = 1700
    h = 1000
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    font = pygame.font.Font(None, 80)
    score_text = font.render(name, 1, (0, 0, 0))
    screen.blit(score_text, (460,300))
    pygame.display.flip()

                
