import pygame
import sys
pygame.init()

class Input:
   def __init__(self):
      self.shift = False
      self.white = (255,255,255)
      self.red = (255,10,10)
      self.black = (0,0,0)

   def get_key(self):
      while True:
         event = pygame.event.poll()
         if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
         elif event.type == pygame.KEYDOWN:
            #print(event.key)
            if event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT]:
               self.shift = True
               continue

            if self.shift:
               #return ascii code
               if event.key >= 97 and event.key <= 122:
                  return event.key - 32
               elif event.key == 50:
                  return 64 #return @
               elif event.key == 32:
                  return 32 #return space even if shifted

            elif not self.shift:
               return event.key
         elif event.type == pygame.KEYUP:
            if event.key in [pygame.K_LSHIFT, pygame.K_RSHIFT]:
               self.shift = False
         else:
            pass

   def display_box(self, screen, message):
      fontobject = pygame.font.Font(None, 40)
      pygame.draw.rect(screen, self.white,
         ((screen.get_width()) - 0, (screen.get_height() / 2) - 0, 0,0)) #if border add 1 for transp
      if len(message) != 0:
         screen.blit(fontobject.render(message, 1 , self.black),
            ((screen.get_width() / 4) - 100, (screen.get_height() / 4) - 10))
      pygame.display.update()

   def ask(self, screen, question):
      current_string = []
      self.display_box(screen, question + ': ' + ''.join(current_string))
      while True:
         inkey = self.get_key()
         if inkey == pygame.K_BACKSPACE:
            current_string = current_string[0:-1]
         elif inkey == pygame.K_RETURN:
            break
         else:
            current_string.append(chr(inkey))
         self.display_box(screen, question + ': ' + ''.join(current_string))
      return ''.join(current_string)

def name(player: int):
   input_box = Input()
   white = (255,255,255)
   screen = pygame.display.set_mode((1700,1000))
   x = 0
   y = 0
   if player == 1:
      redSquare = pygame.image.load('player1.png')
   elif player == 2:
      redSquare = pygame.image.load('player2.png')
   elif player == 3:
      redSquare = pygame.image.load('player3.png')
   elif player == 4:
      redSquare = pygame.image.load('player4.png')
   elif player == 5:
      redSquare = pygame.image.load('player5.png')
   elif player == 6:
      redSquare = pygame.image.load('player6.png')


   screen.blit(redSquare, (x, y))
   pygame.display.flip()
   var = input_box.ask(screen, 'Name')
   print(var + ' was entered')

   return var

