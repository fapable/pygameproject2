def roll_a_dice():
    dice = random.randrange(1, 6);
    return dice

def display_dice(first):
    display_first(first)

def display_first(first):
    if (first == 1):
        gameDisplay.blit(dice_one, (width / 4, 0))
    elif (first == 2):
        gameDisplay.blit(dice_two, (width / 4, 0))
    elif (first == 3):
        gameDisplay.blit(dice_three, (width / 4, 0))
    elif (first == 4):
        gameDisplay.blit(dice_four, (width / 4, 0))
    elif (first == 5):
        gameDisplay.blit(dice_five, (width / 4, 0))
    elif (first == 6):
        gameDisplay.blit(dice_six, (width / 4, 0))

def produce_button_message(text):
    our_font = pygame.font.SysFont("monospace", 15)
    # render the text now
    produce_text = our_font.render(text, 1, red)
    screen.blit(produce_text, (width / 8, height / 5))


#our roll will display message with our roll converted to text form, alongside
def before_roll():
    produce_button_message("Please hit space to roll your dice")

def roll():
    text = "You've completed your roll " + str(dice) + "."
    print(text)
    produce_roll_message(text)

def worp():
    # We don't want our roll value output before the first roll occurs.
    already_rolled = False
    roll_occur = False
    while already_rolled == False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                already_rolled = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    droll = roll_a_dice()
                    roll_occur = True

        before_roll()
        display_dice(droll)
        if roll_occur:
            roll()
