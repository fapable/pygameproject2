def music():

        pygame.mixer.music.load("geluid/jaws.mp3")
        pygame.mixer.music.play(loops = 0, start = .55)
        pygame.mixer.music.set_volume(0.5)
def HoofdmenuNL():
    redSquare = pygame.image.load('MENU.png')
    white = (255,255,255)
    w = 1700
    h = 1000
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))
    x = 0
    y = 0
    black = (0,0,0)
    screen.blit(redSquare, (x, y))
     # Draw the score t
    pygame.display.flip()
    choose = dm.dumbmenu(screen, ['Start Game',
                                        'Opties',
                                        'Handleiding',
                                        'Highscore',
                                        'Stop Game'], 200,150,None,35,1.4,black ,black)

    if choose == 0:
        Players()
        print ("Je hebt gekozen voor 'Start Game'.")
    elif choose == 1:
        opties()
        print ("Je hebt gekozen voor  'Opties'.")
    elif choose == 2:
        story()
        print( "Je hebt gekozen voor 'Handleiding'.")
    elif choose == 3:
        scherm()
        print ("Je hebt gekozen voor  'Highscore'.")
    elif choose == 4:
        print ("Je hebt gekozen voor 'Het stoppen van de Game'.")
pygame.init()
def Players():

    redSquare = pygame.image.load('achtergrondSpelers.png')
    white = (255,255,255)
    w = 1700
    h = 1000
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    black = (0,0,0)


    choose = dm.dumbmenu(screen,[
                            '- 3 spelers',
                            '- 4 spelers',
                            '- 5 spelers',
                            '- 6 spelers',
                            '- terug naar het menu']
                            , 200,150,None,35,1.4,black ,black)


    if choose == 0:
        program()

        print ("Je hebt gekozen voor 3 spelers.")
    elif choose == 1:
        A.program2()
        print ("Je hebt gekozen voor 4 spelers'.")
    elif choose == 2:
        V.program3()
        print( "Je hebt gekozen voor 5 spelers'.")
    elif choose == 3:
        program4()
        print ("Je hebt gekozen voor 6 spelers'.")
    elif choose == 5:
        HoofdmenuNL()
        print('Je hebt gekozen voor terug naar menu ')
def opties():

    redSquare = pygame.image.load('achtergrondopties.png')
    white = (255,255,255)
    w = 1700
    h = 1000
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    black = (0,0,0)

    choose = dm.dumbmenu(screen,[
                            'Geluid uit',
                            'Taal wijzigen -> Engels',
                            'Terug naar het menu']
                            , 180,150,None,35,1.4,black ,black)


    if choose == 0:
        HoofdmenuNL()
        pygame.mixer.music.stop
        print ("Je hebt gekozen voor Geluid uit'.")
    elif choose == 1:
        menuENG()
        print ("Je hebt gekozen voor Taal wijzigen naar het engels''.")
    elif choose == 2:
        HoofdmenuNL()
        print( "Je hebt gekozen voor Terug naar het menu'.")
def story():

    redSquare = pygame.image.load('Story.png')
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels()
def regels():

    redSquare = pygame.image.load('Naamloos.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels2()
def regels2():

    redSquare = pygame.image.load('Regels2.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels3()
def regels3():

    redSquare = pygame.image.load('Regels3.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels4()
def regels4():

    redSquare = pygame.image.load('surprisekaart.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels5()
def regels5():

    redSquare = pygame.image.load('Questregels2.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels6()
def regels6():

    redSquare = pygame.image.load('Powerupregels.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels7()
def regels7():

    redSquare = pygame.image.load('Powerupregels2.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels8()
def regels8():

    redSquare = pygame.image.load('Battleregels.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels9()
def regels9():

    redSquare = pygame.image.load('Battleregels2.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels10()
def regels10():

    redSquare = pygame.image.load('Battleregels3.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()


    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    HoofdmenuNL()
                    print('Einde terug naar menu')
def regels11():

    redSquare = pygame.image.load('Howtoplay.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels12()
def regels12():

    redSquare = pygame.image.load('Howtoplay2.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels13()
def regels13():

    redSquare = pygame.image.load('Howtoplay3.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels14()
def regels14():

    redSquare = pygame.image.load('Howtoplay4.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels15()
def regels15():

    redSquare = pygame.image.load('Howtoplay5.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    story()
def story():

    redSquare = pygame.image.load('Story.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels()
pygame.init()
########################################################
###########################################################
def menuENG():
    redSquare = pygame.image.load('MENU.png')
    white = (255,255,255)
    w = 1700
    h = 1000
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))
    x = 0
    y = 0
    black = (0,0,0)
    screen.blit(redSquare, (x, y))
     # Draw the score t
    pygame.display.flip()
    choose = dm.dumbmenu(screen, ['Start Game',
                                        'Options',
                                        'Manual',
                                        'Show Highscore',
                                        'Quit Game'], 200,150,None,35,1.4,black ,black)

    if choose == 0:
        Playerseng()
        print ("You choose 'Start Game'.")
    elif choose == 1:
        optieseng()
        print ("You choose 'Options'.")
    elif choose == 2:
        storyeng()
        print( "You choose 'Manual'.")
    elif choose == 3:
        scherm()
        print ("You choose 'Show Highscore'.")
    elif choose == 4:
        print ("You choose 'Quit Game'.")
pygame.init()
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


    running = True

    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.K_KP_ENTER:
                    HoofdmenuNL()
def Playerseng():

    redSquare = pygame.image.load('achtergrondopties.png')
    white = (255,255,255)
    w = 1700
    h = 1000
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    black = (0,0,0)


    choose = dm.dumbmenu(screen,[
                            '- 3 players',
                            '- 4 players',
                            '- 5 players', '- 6 players',
                            '- Back to Menu']
                            , 200,150,None,35,1.4,black ,black)


    if choose == 0:
        program()

        print ("You choose '3 players'.")
    elif choose == 1:
        A.program2()
        print ("You choose '4 players'.")
    elif choose == 2:
        V.program3()
        print("You choose '5 players'.")
    elif choose == 3:
        program4()
        print ("You choose '6 players'.")
    elif choose == 5:
        menuENG()
        print("You choose 'Back to Menu'.")
def optieseng():

    redSquare = pygame.image.load('achtergrondopties.png')
    white = (255,255,255)
    w = 1700
    h = 1000
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    black = (0,0,0)

    choose = dm.dumbmenu(screen,[
                            'Sound off/on',
                            'Change -> Engels/Dutch',
                            'Back to Menu']
                            , 180,150,None,35,1.4,black ,black)


    if choose == 0:
        menuENG()
        pygame.mixer.music.stop
        print ("You choose 'Sound off/on'.")
    elif choose == 1:
        HoofdmenuNL()
        print ("You choose 'Change -> Engels/Dutch'.")
    elif choose == 2:
        menuENG()
        print( "You choose 'Back to Menu'.")
def regelseng():

    redSquare = pygame.image.load('regels1ENG.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels2eng()
def regels2eng():

    redSquare = pygame.image.load('regels2ENG.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels3eng()
def regels3eng():

    redSquare = pygame.image.load('regels3ENG.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels4eng()
def regels4eng():

    redSquare = pygame.image.load('rules.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels5eng()
def regels5eng():

    redSquare = pygame.image.load('surprise.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels6eng()
def regels6eng():

    redSquare = pygame.image.load('quest.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels7eng()
def regels7eng():

    redSquare = pygame.image.load('power.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regels8eng()
def regels8eng():

    redSquare = pygame.image.load('battle.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()


    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    menuENG()
                    print('Einde terug naar menu')
def storyeng():

    redSquare = pygame.image.load('storyENG.png')
    clock = pygame.time.Clock()
    white = (255, 64, 64)
    w = 810
    h = 420
    screen = pygame.display.set_mode((w, h))
    screen.fill((white))

    screen.fill((white))
    x = 0
    y = 0
    screen.blit(redSquare, (x, y))
    pygame.display.flip()

    running = True
    while (running):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if redSquare.get_rect().collidepoint(x, y):
                    regelseng()

music()
HoofdmenuNL()
