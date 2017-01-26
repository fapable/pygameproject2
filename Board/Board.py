import pygame
#Define the lists
normale_vakjes = [(2,0),(3,0),(5,0),(6,0),(7,0),(8,0),(9,0),(10,0),(11,0),(13,0),(14,0),(17,0),(18,0),(19,0),(20,0),(22,0),(23,0),(24,0),(25,0),(27,0),(28,0),(29,0),(30,0),(31,0),(1,2),(1,8),(1,12),(2,2),(2,12),(2,31),(3,2),(3,12,),(3,13),(3,15),(3,18),(3,19),(4,2),(4,14),(4,24),(4,26),(4,27),(4,31),(5,12)]

#class position
class Vakjes:
    def __init__(self,position,row,column):
        self.Pos = position
        self.x = row
        self.y = column

    def draw(self,screen):
        pygame.draw.rect(screen, color, (self.x,self.y,WIDTH,HEIGHT), 0)

class Vector:
    def __init__(self,x,y):
        self.PosX = x
        self.PosY = y

# Define some colors

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 43
HEIGHT = 43

# This sets the margin between each cell
MARGIN = 5

# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(20):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for column in range(40):
        grid[row].append(0)  # Append a cell




# Initialize pygame
pygame.init()

# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [1700 , 1000]
screen = pygame.display.set_mode(WINDOW_SIZE)

# Set title of screen
pygame.display.set_caption("Ontsnapperdam")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)

    # Set the screen background
    screen.fill(BLACK)
    # Draw the grid

    for row in range(0,20):
        for column in range(0,35):
            for i in normale_vakjes:
                Vakjes(i,row,column)
                if (column,row) == i :
                    Vakjes(i,row,column)
                    pygame.draw.rect(screen,
                             GREEN,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
                else:
                    pygame.draw.rect(screen,
                             WHITE,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])

    clock.tick(60)


    pygame.display.flip()


pygame.quit()
